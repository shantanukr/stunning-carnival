# server.py
from fastapi import FastAPI, Request
from tools import get_weather

app = FastAPI()


@app.post("/tool/get_weather")
async def call_get_weather(request: Request):
    body = await request.json()
    city = body.get("city", "Unknown")
    return {"result": get_weather(city)}
