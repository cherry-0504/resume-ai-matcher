# AI 简历诊断与岗位匹配助手

基于 **FastAPI**、**PyMuPDF**、**HTML / Tailwind CSS** 与 **OpenAI 兼容大模型接口（硅基流动 `Qwen/Qwen2.5-7B-Instruct`）** 开发的简历诊断与人岗匹配工具。用户上传 PDF 格式简历并粘贴目标岗位 JD 后，系统自动提取简历文本并调用大模型分析，生成岗位匹配度评分、整体评价、已命中优势技能、建议补齐关键词以及针对性修改与润色建议。

---

## 一、项目背景与定位

在求职投递过程中，同一份简历面对不同岗位的 JD 时，往往存在关键词匹配度不足、核心优势不够突出或项目表达偏流水账等问题。本项目旨在通过轻量级前后端架构与大模型能力，帮助求职者快速定位简历与目标岗位的差距，并提供可落地的修改参考。

---

## 二、核心功能

* **PDF 简历解析**：基于 `PyMuPDF` 提取 PDF 简历中的文本内容，作为后续分析输入。
* **人岗匹配评估**：结合目标岗位 JD 输出匹配度评分、候选人综合评价、已命中优势技能与建议补齐关键词。
* **针对性润色建议**：针对薄弱环节给出修改方向与可参考的润色表达示例。
* **轻量 Web 交互**：后端采用 `FastAPI` 提供接口，前端使用 `HTML` 与 `Tailwind CSS` 展示诊断结果。

---

## 三、技术栈

| 模块 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| **后端框架** | FastAPI + Uvicorn | 提供 Web 服务与诊断接口 |
| **文档解析** | PyMuPDF | 解析上传的 PDF 简历文本 |
| **大模型调用** | OpenAI SDK + 硅基流动 API | 使用 `Qwen/Qwen2.5-7B-Instruct` 生成诊断与润色建议 |
| **环境配置** | python-dotenv | 从 `.env` 读取 API Key 与接口地址 |
| **前端界面** | HTML + Tailwind CSS | 表单输入与匹配结果可视化展示 |

---

## 四、系统实现流程

上传 PDF 简历与输入岗位 JD → 后端解析 PDF 文本 → 拼接 Prompt 调用大模型接口 → 结构化返回匹配分数、关键词与润色建议 → 前端页面展示诊断结果

---

## 五、目录结构与配置说明

```text
resume-ai-matcher/
├── .env.example          # 环境变量模板（不含真实密钥，本地需复制为 .env）
├── assets/
│   └── demo-result.png   # 系统运行与诊断结果演示截图
├── backend/
│   └── main.py           # FastAPI 后端、PDF 解析与大模型分析逻辑
└── frontend/
    └── index.html        # 前端交互与诊断结果展示页面
```

> 注意：仓库中仅提供 `.env.example` 模板，真实的 `.env` 密钥与本地 `venv/` 虚拟环境不会上传至代码仓库。

---

## 六、项目演示与本地运行

本项目当前为本地启动运行的 Web 应用，可通过以下步骤快速完成本地演示：

1. **创建虚拟环境并安装依赖**
   在本地终端进入 `backend` 目录执行：
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install fastapi uvicorn pymupdf openai python-multipart python-dotenv
   ```

2. **配置环境变量**
   将项目根目录的 `.env.example` 复制一份并重命名为 `.env`，填入你的硅基流动 API Key 与接口配置：
   ```env
   OPENAI_API_KEY=your_siliconflow_api_key_here
   OPENAI_BASE_URL=[https://api.siliconflow.cn/v1](https://api.siliconflow.cn/v1)
   MODEL_NAME=Qwen/Qwen2.5-7B-Instruct
   ```

3. **启动服务并打开页面**
   在 `backend` 目录下运行：
   ```bash
   uvicorn main:app --reload
   ```
   服务启动后，打开浏览器访问 `http://127.0.0.1:8000`，上传测试 PDF 简历并填入目标岗位 JD，点击“开始智能诊断”即可查看分析结果。

---

## 七、系统运行截图

![简历诊断与岗位匹配结果演示](assets/demo-result.png)

---

## 八、后续扩展方向

* 接入 **SQLite** 保存历史诊断记录，支持对比不同版本简历的匹配分数变化。
* 增加一键复制润色建议或导出诊断报告功能。
* 进一步细化 JD 技能权重拆解与多岗位批量对比能力。
