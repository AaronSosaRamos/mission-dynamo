from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

from services.genai import YoutubeProcessor, GeminiProcessor
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../authentication.json"

class VideoAnalysisRequest(BaseModel):
    youtube_link: HttpUrl
    #advanced settings

app = FastAPI()

#Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gen_ai_processor = GeminiProcessor(
    model_name='gemini-pro',
    project = 'mission-dynamo-imp'
)

@app.get("/")
def health():
    return {"status": "OK"}

@app.post("/analyze_video")
def analyze_video(request: VideoAnalysisRequest):
    #Doing the analysis

    processor = YoutubeProcessor(gen_ai_processor)
    result = processor.retrieve_youtube_documents(str(request.youtube_link), verbose=True)

    #summary = gen_ai_processor.generate_document_summary(result)

    #Find key concepts
    key_concepts = processor.find_key_concepts(result, verbose=True)

    return {
        "key_concepts": key_concepts
    }