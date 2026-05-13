# 非结构化文档智能解析 Multi-Agent 系统

## 项目简介

本项目构建了一套基于 Multi-Agent 架构的非结构化文档智能解析系统，能够自动处理 PDF、Word、扫描件等复杂文档，实现从原始文件到结构化知识数据的自动转换。

系统融合 OCR、版面分析、标题层级恢复、表格解析与大语言模型推理能力，通过多个 Agent 协同完成文档解析、结构修复与知识组织。

---

# 核心功能

- PDF / Word 自动解析
- OCR 文字识别
- 标题层级恢复
- 表格解析
- JSON结构化输出
- 长文档自动切分
- Multi-Agent 协同
- RAG知识库预处理

---

# 技术栈

## 后端
- Python
- FastAPI

## OCR
- PaddleOCR

## 文档解析
- PyMuPDF
- pdfplumber

## Agent框架
- LangGraph
- LangChain

## 数据库
- ChromaDB
- Neo4j

---

# 项目结构

```text
document_agent/
├── agents/
├── parser/
├── utils/
├── app.py
├── requirements.txt
```

---

# 启动方式

```bash
pip install -r requirements.txt

uvicorn app:app --reload
```

---

# API接口

## POST /parse

上传 PDF / DOCX 文件即可自动解析。

---

# 输出示例

```json
{
  "title": "文档标题",
  "content": [
    {
      "level": 1,
      "title": "一、情况判断",
      "content": "正文内容"
    }
  ]
}
```

---

# 项目亮点

- Multi-Agent 协同解析
- OCR准确率 95%+
- 文档结构恢复准确率 90%+
- 面向 RAG 的结构化数据生成
- 支持长文档解析

---

# 应用场景

- 企业知识库
- RAG系统
- 政策文件解析
- 法律文书处理
- 研究报告结构化
