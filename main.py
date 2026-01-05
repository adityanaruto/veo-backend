from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

class VideoRequest(BaseModel):
    prompt: str

@app.get("/")
def health_check():
    return {"status": "Backend is running"}

@app.post("/generate-video")
def generate_video(data: VideoRequest):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    operation = genai.models.generate_videos(
        model="veo-3.1-generate-preview",
        prompt=data.prompt,
        config={
            "fps": 24,
            "aspect_ratio": "9:16"
        }
    )

    result = operation.resolve()
    return {"result": result}
