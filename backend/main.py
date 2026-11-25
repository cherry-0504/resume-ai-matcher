import json
import os
from pathlib import Path

import fitz
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

app = FastAPI(title="AI 简历诊断与岗位匹配助手 V1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def extract_text_from_pdf(file_bytes: bytes) -> str:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    pages_text = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            pages_text.append(f"--- 第 {i + 1} 页 ---\n{text}")
    doc.close()
    return "\n\n".join(pages_text)


def get_llm_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.siliconflow.cn/v1").strip()
    if not api_key or api_key.startswith("你刚复制"):
        raise HTTPException(status_code=400, detail="请先在 .env 文件中填入有效的 OPENAI_API_KEY")
    return OpenAI(api_key=api_key, base_url=base_url)


@app.get("/")
def serve_frontend():
    html_path = BASE_DIR / "frontend" / "index.html"
    return FileResponse(html_path)


@app.post("/api/analyze")
async def analyze_resume(
    resume_file: UploadFile = File(...),
    jd_text: str = Form(...),
):
    if not resume_file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="目前仅支持上传 PDF 格式的简历")
    if not jd_text.strip():
        raise HTTPException(status_code=400, detail="请粘贴目标岗位的 JD（职位描述）")

    file_bytes = await resume_file.read()
    resume_text = extract_text_from_pdf(file_bytes)
    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="未能从 PDF 中提取到文字（可能是扫描件图片，请换纯文本 PDF）")

    client = get_llm_client()
    model_name = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct").strip()

    prompt = f"""你是一位资深技术招聘官与简历优化专家。请对比【候选人简历】与【目标岗位 JD】，给出客观、犀利且可落地的诊断结果。

请严格按照以下 JSON 格式输出（不要包含 ```json 或多余解释）：
{{
  "match_score": 75,
  "summary": "一句话总结当前匹配度与核心短板",
  "matched_skills": ["技能1", "技能2"],
  "missing_skills": ["缺失技能1", "缺失技能2"],
  "suggestions": [
    {{
      "section": "项目经历 / 技能栈 / 教育背景",
      "issue": "当前存在的问题",
      "rewrite_example": "按 STAR 法则优化后的表达示例"
    }}
  ]
}}

【目标岗位 JD】：
{jd_text}

【候选人简历】：
{resume_text[:8000]}
"""

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "你只输出合法的 JSON 对象，不输出 Markdown 代码块标记。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        raw_content = response.choices[0].message.content.strip()
        if raw_content.startswith("```"):
            raw_content = raw_content.split("\n", 1)[-1]
        if raw_content.endswith("```"):
            raw_content = raw_content.rsplit("```", 1)[0]
        result_data = json.loads(raw_content.strip())
        return {"status": "success", "data": result_data}
    except json.JSONDecodeError:
        return {
            "status": "raw_text",
            "raw_content": raw_content,
            "message": "模型返回了非标准 JSON，已为你展示原始建议",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"调用模型失败：{str(e)}")
