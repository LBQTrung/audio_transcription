from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import whisper
from typing import List
import asyncio
import torch
from tqdm import tqdm
import os
import uuid

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device if device != 'cuda' else torch.cuda.get_device_name(0)}")
model = whisper.load_model("small", device=device)

# Serve the HTML interface
@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Transcription route
@app.post("/transcribe/")
async def transcribe_audios(files: List[UploadFile] = File(...)):
    transcriptions = []
    unique_code = uuid.uuid4()
    file_index = 0

    os.makedirs("audios", exist_ok=True)
    os.makedirs("texts", exist_ok=True)

    async def process_file(file: UploadFile):
        audio_data = await file.read()
        unique_filename = f"audios/{unique_code}_{file_index}.mp3"
        with open(unique_filename, "wb") as f:
            f.write(audio_data)
        result = model.transcribe(unique_filename)
        transcriptions.append({"filename": file.filename, "text": result["text"]})
        
        transcription_filename = f"texts/{unique_code}_{file_index}.txt"
        with open(transcription_filename, "w", encoding="utf-8") as f:
            f.write(result["text"])

        # os.remove(unique_filename)  # Delete the file after transcription

    for file in tqdm(files, desc="Transcribing files"):
        await process_file(file)
        file_index += 1

    return {"transcriptions": transcriptions}