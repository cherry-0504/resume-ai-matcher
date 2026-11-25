<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI 简历诊断与岗位匹配助手 V1.0</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen">
  <div class="max-w-5xl mx-auto px-4 py-10">
    <div class="mb-8 text-center">
      <span class="inline-block px-3 py-1 text-xs font-semibold bg-indigo-100 text-indigo-700 rounded-full mb-2">
        毕设 & 求职作品集 V1.0
      </span>
      <h1 class="text-3xl font-bold text-slate-900">基于 LLM 的智能简历诊断与岗位匹配助手</h1>
      <p class="text-slate-500 mt-2">上传 PDF 简历并粘贴岗位 JD，快速定位匹配差距与 STAR 润色建议</p >
    </div>

    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 space-y-6">
      <div>
        <label class="block text-sm font-semibold text-slate-700 mb-2">1. 上传 PDF 简历</label>
        <input
          id="resumeFile"
          type="file"
          accept=".pdf"
          class="block w-full text-sm text-slate-600 file:mr-4 file:py-2.5 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 cursor-pointer"
        />
      </div>

      <div>
        <label class="block text-sm font-semibold text-slate-700 mb-2">2. 粘贴目标岗位 JD</label>
        <textarea
          id="jdText"
          rows="6"
          placeholder="例如：熟悉 Python 或前后端开发，了解数据库与接口开发，有项目经验者优先..."
          class="w-full rounded-xl border border-slate-300 p-3.5 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
        ></textarea>
      </div>

      <div class="flex justify-end">
        <button
          id="submitBtn"
          onclick="handleAnalyze()"
          class="px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-medium rounded-xl transition cursor-pointer disabled:opacity-50"
        >
          开始智能诊断
        </button>
      </div>
    </div>

    <div id="errorBox" class="hidden mt-6 p-4 rounded-xl bg-red-50 border border-red-200 text-red-700 text-sm"></div>
    <div id="resultArea" class="hidden mt-8 space-y-6"></div>
  </div>

  <script>
    async function handleAnalyze() {
      const fileInput = document.getElementById("resumeFile");
      const jdInput = document.getElementById("jdText");
      const btn = document.getElementById("submitBtn");
      const errorBox = document.getElementById("errorBox");
      const resultArea = document.getElementById("resultArea");

      errorBox.classList.add("hidden");
      resultArea.classList.add("hidden");

      if (!fileInput.files.length) {
        showError("请先选择一份 PDF 简历文件。");
        return;
      }
      if (!jdInput.value.trim()) {
        showError("请先输入目标岗位的 JD 内容。");
        return;
      }

      const formData = new FormData();
      formData.append("resume_file", fileInput.files[0]);
      formData.append("jd_text", jdInput.value.trim());

      btn.disabled = true;
      btn.textContent = "正在分析中，请稍候...";

      try {
        const res = await fetch("/api/analyze", {
          method: "POST",
          body: formData,
        });
        const payload = await res.json();
        if (!res.ok) {
          throw new Error(payload.detail || "请求失败");
        }
        renderResult(payload);
      } catch (err) {
        showError(err.message);
      } finally {
        btn.disabled = false;
        btn.textContent = "开始智能诊断";
      }
    }

    function showError(msg) {
      const errorBox = document.getElementById("errorBox");
      errorBox.textContent = msg;
      errorBox.classList.remove("hidden");
    }

    function renderResult(payload) {
      const resultArea = document.getElementById("resultArea");
      resultArea.classList.remove("hidden");

      if (payload.status === "raw_text") {
        resultArea.innerHTML = `
          <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
            <h2 class="text-lg font-bold mb-3">${escapeHtml(payload.message)}</h2>
            <pre class="whitespace-pre-wrap text-sm text-slate-700 bg-slate-50 p-4 rounded-xl">${escapeHtml(payload.raw_content)}</pre>
          </div>
        `;
        return;
      }

      const d = payload.data;
      const matchedHtml = (d.matched_skills || [])
        .map(s => `<span class="px-3 py-1 text-xs font-medium rounded-full bg-emerald-100 text-emerald-800">${escapeHtml(s)}</span>`)
        .join("");
      const missingHtml = (d.missing_skills || [])
        .map(s => `<span class="px-3 py-1 text-xs font-medium rounded-full bg-amber-100 text-amber-800">${escapeHtml(s)}</span>`)
        .join("");

      const suggestionsHtml = (d.suggestions || [])
        .map((item, idx) => `
          <div class="border border-slate-200 rounded-xl p-4 space-y-2 bg-slate-50/60">
            <div class="text-xs font-semibold text-indigo-600 uppercase">建议 ${idx + 1} · ${escapeHtml(item.section || "")}</div>
            <div class="text-sm text-slate-700"><span class="font-semibold">问题：</span>${escapeHtml(item.issue || "")}</div>
            <div class="text-sm text-slate-800 bg-white p-3 rounded-lg border border-slate-200">
              <span class="font-semibold text-emerald-700">润色参考：</span>${escapeHtml(item.rewrite_example || "")}
            </div>
          </div>
        `)
        .join("");

      resultArea.innerHTML = `
        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-slate-100 pb-5">
            <div>
              <div class="text-sm text-slate-500">岗位匹配度评估</div>
              <div class="text-4xl font-extrabold text-indigo-600 mt-1">${escapeHtml(String(d.match_score ?? "--"))} <span class="text-lg font-normal text-slate-400">/ 100</span></div>
            </div>
            <p class="text-sm text-slate-700 max-w-2xl bg-indigo-50/70 p-4 rounded-xl">${escapeHtml(d.summary || "")}</p >
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 class="text-sm font-semibold text-slate-700 mb-2.5">已命中优势技能</h3>
              <div class="flex flex-wrap gap-2">${matchedHtml || '<span class="text-xs text-slate-400">暂无</span>'}</div>
            </div>
            <div>
              <h3 class="text-sm font-semibold text-slate-700 mb-2.5">建议补齐/突出关键词</h3>
              <div class="flex flex-wrap gap-2">${missingHtml || '<span class="text-xs text-slate-400">暂无</span>'}</div>
            </div>
          </div>

          <div>
            <h3 class="text-base font-bold text-slate-900 mb-3">针对性修改与润色建议</h3>
            <div class="space-y-3">${suggestionsHtml}</div>
          </div>
        </div>
      `;
    }

    function escapeHtml(str) {
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }
  </script>
</body>
</html>
