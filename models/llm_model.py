import os
from dotenv import load_dotenv
from xhtml2pdf import pisa
from io import BytesIO
from .prompts import get_prompt, read_file_to_string
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    api_key=GOOGLE_API_KEY,
    model="gemini-1.5-flash-002",
    temperature=0.8,
    max_tokens=None,
    timeout=None
)
print("ChatGoogleGenerativeAI model loaded successfully!")


async def generate_report(text, database, language):
    prompt_template, full_prompt = get_prompt(text, database, language)
    chain = prompt_template | llm

    response = chain.invoke(full_prompt)

    return response.content


def create_pdf_from_html(html_content: str) -> BytesIO:
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
    
    if pisa_status.err:
        raise Exception("Error occurred while generating the PDF.")
    
    pdf_buffer.seek(0)
    return pdf_buffer