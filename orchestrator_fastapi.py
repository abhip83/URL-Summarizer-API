#!/usr/bin/env python3
import os, time, asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawler_simple import crawl_url
from summarizer_simple import summarize_text
import uvicorn
app = FastAPI()

class Request(BaseModel):
    url: str

@app.post("/summarize")
async def summarize_url(req: Request):
    if not req.url.strip():
        raise HTTPException(status_code=400, detail="Missing URL")

    start = time.time()
    try:
        # Step 1: Crawl
        crawl_result = await crawl_url(req.url)
        text = crawl_result.get("text", "")
        print("scraped_data########",text)
        if not text.strip():
            raise HTTPException(status_code=500, detail="No text extracted from page")
        # Step 2: Summarize
        summary = await asyncio.to_thread(summarize_text, text[:5000])
        print("Summarry++++++++",summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "url": req.url,
        "summary": summary.get("summary", ""),
        "original_length": summary.get("original_length", 0),
        "summary_length": summary.get("summary_length", 0),
        "duration": round(time.time() - start, 2),
    }


# uvicorn orchestrator_fastapi:app --host 0.0.0.0 --port 8000