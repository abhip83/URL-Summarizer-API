#!/usr/bin/env python3
import os
from typing import Dict
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"

def summarize_text(text: str, min_words: int = 20, max_words: int = 120) -> Dict[str, str]:
    if not text.strip():
        return {"summary": "", "original_length": 0, "summary_length": 0}

    prompt = f"Summarize the following text in {min_words}-{max_words} words:\n\n{text}"
    try:
        resp = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        summary = resp["choices"][0]["message"]["content"].strip()
        return {
            "summary": summary,
            "original_length": len(text),
            "summary_length": len(summary),
        }
    except Exception as e:
        return {"summary": "", "original_length": len(text), "summary_length": 0, "error": str(e)}

if __name__ == "__main__":
    sample_text = """Turning to the UN Security Council, Guterres says it must live up to its responsibilities, be more transparent and tackle injustices.
He adds "we must choose human dignity and human rights" as he now addresses the assembly in French, after starting in English.
Guterres says reforms are needed to the international finance system and calls for "the greater participation of developing countries in terms of their composition and their decision-making."
The secretary general is now talking about the need for climate action. "Fossil fuels are a losing bet", he tells the assembly, calling on G20 industrialised countries to commit to emission reductions.
"We have the solutions and tools but we must choose climate justice and climate action," he says"""
    print(summarize_text(sample_text))
