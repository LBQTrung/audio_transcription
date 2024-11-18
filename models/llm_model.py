from langflow.load import run_flow_from_json
from xhtml2pdf import pisa
from io import BytesIO
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read GOOGLE_API_KEY from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TWEAKS = {
  "Prompt-KYPlF": {
    "Document": "",
    "template": "Write a report in {Language} based on the following Database, Document, Requirements and HTML Format:\n---\nDatabase:\n{Database}\n---\n\n---\nDocument:\n{Document}\n---\n\nRequirements :\n{Requirements}\n\n---\nHTML Format:\n{Htmlformat}\n\n\nAnswer:\n",
    "Database": "",
    "Language": "",
    "Requirements": "",
    "Htmlformat": ""
  },
  "ParseData-f9hBM": {
    "sep": "\n",
    "template": "{text}"
  },
  "File-51d1E": {
    "path": "real_estate2.txt",
    "silent_errors": False
  },
  "TextInput-G353c": {
    "input_value": "Please extract and provide the following details for each component of the property:\nDate: [Date of Assessment]\nArea Assessed: [Area Assessed]\nLocation: [Detail Location]\nAssessor: [Your Name]\nDescription: list each component of the property and its description (e.g., living space, bedrooms, backyard, garage, etc.).\nCondition Assessment: For each component listed in the Description, provide the following information:\n- Positive: List any positive aspects or conditions of the component.\n- Negative: List any negative aspects or conditions of the component.\n- Recommendations: Provide any recommendations for improvement, maintenance, or changes needed.\nOverall Assessment: Provide a general evaluation of the property's condition based on the above information. Summarize if the property is in good condition, requires improvements, or needs any specific attention.\nNext Steps: List the next steps required for maintenance, repairs, or other actions to be taken for the property, based on the assessment.\n\nEnsure the output is always in pure HTML format, exactly as in htmlformat style without any additional characters such as \"```html\" at the start or \"```\" at the end, minimizing line breaks as much as possible."
  },
  "GoogleGenerativeAIModel-Y5YQH": {
    "google_api_key": "{GOOGLE_API_KEY}",
    "input_value": "",
    "max_output_tokens": None,
    "model": "gemini-1.5-flash",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  },
  "File-vxvhj": {
    "path": "database.txt",
    "silent_errors": False
  },
  "ParseData-gipf5": {
    "sep": "\n",
    "template": "{text}"
  },
  "TextInput-kX0LZ": {
    "input_value": "english"
  },
  "TextOutput-sojQq": {
    "input_value": ""
  },
  "TextInput-NmG9p": {
    "input_value": "<!DOCTYPE html><html>\n<head> <title>Property Assessment Report</title> <style> * { box-sizing: border-box; margin: 0; padding: 0; } body { font-family: Arial, sans-serif; font-size: 13px; box-sizing: border-box; margin: 0; padding: 0 30px 0; } h1 { font-size: 20px; line-height: 0; margin-bottom: 30px; text-align: center; color: #fff; padding: 20px; background-color: #4C99E6; } .general-info { margin-bottom: 5px; font-size: 15px; } h2 { font-size: 15px; margin-top: 20px; margin-bottom: 10px; } h3 { font-size: 14px; margin-top: 15px; margin-bottom: 10px; } </style></head>\n<body> <h1 class=\"title\">Property Assessment Report</h1> <p class=\"general-info\"><b>Date:</b> 11/11/2024</p> <p class=\"general-info\"><b>Area Assessed:</b> Interior Hallway</p> <p class=\"general-info\"><b>Location:</b> 4248 Windsor Street</p> <p class=\"general-info\"><b>Assessor:</b> Trung Jr</p> <h2>Description</h2> <p>The property at 4248 Windsor Street is a brand new construction half-duplex. It features:</p> <ul> <li><strong>Living Space:</strong> Open and airy living space with double doors leading to a large deck, creating an indoor-outdoor living experience.</li> <li><strong>Bedrooms:</strong> Three bedrooms located on the third floor. Each bedroom has a balcony.</li> <li><strong>Balconies:</strong> Balconies are accessible from each bedroom, including a shared balcony between two bedrooms.</li> <li><strong>Backyard:</strong> The property includes a backyard.</li> <li><strong>Garage:</strong> A single-car garage is located below the main floor.</li> <li><strong>Appliances and Finishes:</strong> High-end appliances and finishes throughout the property, including hardwood floors, marble countertops and backsplash, and \"fancy robot\" toilets.</li> <li><strong>Walk-in Closets:</strong> Two walk-in closets, one in the second bedroom and one in the primary bedroom.</li> <li><strong>En Suite:</strong> The primary bedroom has an en suite bathroom.</li> </ul> <h2>Condition Assessment</h2> <h3>Living Space</h3> <ul> <li><strong>Positive:</strong> Open and airy, large deck, indoor-outdoor living experience.</li> <li><strong>Negative:</strong> None mentioned.</li> <li><strong>Recommendations:</strong> Maintain the open layout and ensure the deck is properly maintained.</li> </ul> <h3>Bedrooms</h3> <ul> <li><strong>Positive:</strong> Spacious, each bedroom has a balcony, walk-in closets in two bedrooms, en suite in the primary bedroom.</li> <li><strong>Negative:</strong> None mentioned.</li> <li><strong>Recommendations:</strong> Ensure proper ventilation and maintenance of balconies and walk-in closets.</li> </ul> <h3>Backyard</h3> <ul> <li><strong>Positive:</strong> The property includes a backyard.</li> <li><strong>Negative:</strong> No specific details about the backyard's size or condition were provided.</li> <li><strong>Recommendations:</strong> Assess the backyard's size, condition, and potential for landscaping or other improvements.</li> </ul> <h3>Garage</h3> <ul> <li><strong>Positive:</strong> Single-car garage.</li> <li><strong>Negative:</strong> No specific details about the garage's condition were provided.</li> <li><strong>Recommendations:</strong> Inspect the garage for any maintenance needs or potential repairs.</li> </ul> <h3>Appliances and Finishes</h3> <ul> <li><strong>Positive:</strong> High-end appliances and finishes, including hardwood floors, marble countertops and backsplash, and \"fancy robot\" toilets.</li> <li><strong>Negative:</strong> None mentioned.</li> <li><strong>Recommendations:</strong> Maintain the high-quality appliances and finishes to preserve their value and functionality.</li> </ul> <h2>Overall Assessment</h2> <p>Based on the information provided, the property appears to be in excellent condition. It is a brand new construction with high-quality finishes and amenities. The open layout, spacious bedrooms, and outdoor spaces make it an attractive option for a growing family or anyone seeking more space.</p> <h2>Next Steps</h2> <ul> <li>Conduct a thorough inspection of the property to verify the condition of all components and identify any potential issues.</li> <li>Assess the backyard's size, condition, and potential for landscaping or other improvements.</li> <li>Inspect the garage for any maintenance needs or potential repairs.</li> <li>Develop a maintenance plan to ensure the continued good condition of the property and its high-quality finishes.</li> </ul></body>\n</html>"
  }
}

TWEAKS["GoogleGenerativeAIModel-Y5YQH"]["google_api_key"] = GOOGLE_API_KEY

async def report_generator(txt_file_path, language="English"):
    home_path = "D:/tenomad_intern/mvp_generate_reports/audio_transcription/"

    # User input
    TWEAKS["File-51d1E"]["path"] = home_path + txt_file_path
    TWEAKS["TextInput-kX0LZ"]["input_value"] = language
    # Simulate query data from database
    TWEAKS["File-vxvhj"]["path"] = home_path + "/models/database.txt"

    outputs = run_flow_from_json(
        flow="models/best_report_generator_15_11_2024.json",
        input_value="message",
        fallback_to_env_vars=False,
        tweaks=TWEAKS,
        output_type="text",
    )

    return outputs[0].outputs[0].results["text"].data["text"]


def create_pdf_from_html(html_content: str) -> BytesIO:
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
    
    # Kiểm tra xem quá trình chuyển đổi có thành công không
    if pisa_status.err:
        raise Exception("Error occurred while generating the PDF.")
    
    pdf_buffer.seek(0)  # Đặt lại con trỏ tệp về đầu buffer
    return pdf_buffer