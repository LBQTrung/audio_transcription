from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
import os
import uuid
from models.llm_model import generate_report, create_pdf_from_html
from pydantic import BaseModel

app = FastAPI()

database = """
Date: 11/11/2024
Area Assessed: Interior Hallway
Location: 4248 Windsor Street
Assessor: Trung Jr
"""

class ReportRequest(BaseModel):
    text: str
    language: str = "English"

# Transcription route
@app.post("/report-generate")
async def transcribe_audios(request: ReportRequest):
    
    report_html = await generate_report(text=request.text, database=database, language=request.language)
    report_pdf = create_pdf_from_html(report_html)
    return StreamingResponse(report_pdf, media_type="application/pdf", headers={"Content-Disposition": "inline; filename=report.pdf"})