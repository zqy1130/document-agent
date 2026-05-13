# 非结构化文档智能解析 Agent

## 功能

- PDF / DOCX 解析
- OCR 识别
- 标题层级恢复
- JSON 结构化
- Multi-Agent 架构
- FastAPI 接口

## 启动

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## 接口

POST /parse

上传 PDF 或 DOCX 文件即可。
