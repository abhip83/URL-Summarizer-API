# 🌐 AI-Powered Web Page Summarizer (FastAPI + Crawl4AI + OpenAI)

An end-to-end **AI-driven web page summarization system** that:
- Crawls live web pages
- Extracts clean, readable content
- Generates concise summaries using Large Language Models
- Exposes everything via a **FastAPI REST API**

This project demonstrates practical skills in **Web Crawling, NLP, Generative AI, Async Programming, and API Development**.

---

## 📂 Project Structure

├── crawler_simple.py # Web crawler logic
├── summarizer_simple.py # OpenAI-based summarizer
├── orchestrator_fastapi.py # FastAPI orchestration layer
├── .env # API keys
└── README.md
---

## 🧠 Key Features

- 🌍 **Asynchronous Web Crawling**
- 🧹 **Noise Removal** (navbars, footers, ads)
- 📝 **Markdown Content Extraction**
- 🤖 **AI-based Text Summarization**
- ⚡ **FastAPI Backend**
- 📊 **Response Metadata** (length, duration)
- 🧪 Easy to test with Postman / Swagger UI
---

## 📄 File Descriptions

### 🔹 `crawler_simple.py`
- Uses **crawl4ai AsyncWebCrawler**
- Removes unwanted HTML elements
- Converts page content into clean markdown
- Fully asynchronous implementation

:contentReference[oaicite:0]{index=0}

---

### 🔹 `summarizer_simple.py`
- Uses **OpenAI ChatCompletion API**
- Converts long text into concise summaries
- Configurable word limits
- Returns metadata such as original and summary length

:contentReference[oaicite:1]{index=1}

---

### 🔹 `orchestrator_fastapi.py`
- FastAPI-based backend
- Accepts URL as input
- Calls crawler → summarizer
- Returns structured JSON response

:contentReference[oaicite:2]{index=2}

---

## ⚙️ Tech Stack

| Category | Technology |
|--------|------------|
| Language | Python 3.9+ |
| Web Framework | FastAPI |
| Web Crawling | crawl4ai |
| AI / NLP | OpenAI GPT |
| Async | asyncio |
| API Server | Uvicorn |
| Env Management | python-dotenv |

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
▶️ Run the Application
uvicorn orchestrator_fastapi:app --host 0.0.0.0 --port 8000
```
🧪 API Usage
Endpoint
POST /summarize

Request Body
{
  "url": "https://www.bbc.com/news"
}

Sample Response
{
  "url": "https://www.bbc.com/news",
  "summary": "The article discusses global political developments...",
  "original_length": 4821,
  "summary_length": 312,
  "duration": 2.41
}

🧩 Example Use Cases

📰 News Article Summarization

📚 Research Paper Previews

🧠 Knowledge Extraction Pipelines

🤖 RAG-based Systems

🧾 Automated Content Intelligence



