# agent.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
MODEL = "sonar"

def call_perplexity(prompt, tools_schema):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "tools": tools_schema,
        "tool_choice": "auto"
    }
    res = requests.post("https://api.perplexity.ai/chat/completions", headers=headers, json=data)
    return res.json()
