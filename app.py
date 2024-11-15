from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import os
import uuid
from models.whisper_model import transcribe_audio
from models.llm_model import report_generator, create_pdf_from_html

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")

# Serve the HTML interface
@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Transcription route
@app.post("/report-generate")
async def transcribe_audios(file: UploadFile = File(...)):
    unique_code = uuid.uuid4()
    os.makedirs("audios", exist_ok=True)
    os.makedirs("texts", exist_ok=True)

    file_name = file.filename.split(".")[0]
    audio_data = await file.read()
    unique_filename = f"audios/{unique_code}_{file_name}.mp3"
    with open(unique_filename, "wb") as f:
        f.write(audio_data)

    text_result = await transcribe_audio(unique_filename)
    transcription_filename = f"texts/{unique_code}_{file_name}.txt"
    with open(transcription_filename, "w", encoding="utf-8") as f:
        f.write(text_result) 
    # os.remove(unique_filename)
    
    report_html = await report_generator(transcription_filename)
    report_pdf = create_pdf_from_html(report_html)
    return StreamingResponse(report_pdf, media_type="application/pdf", headers={"Content-Disposition": "inline; filename=report.pdf"})