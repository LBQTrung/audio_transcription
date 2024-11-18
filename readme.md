# Whisper Transcription Service

This project is a web-based transcription service using FastAPI and OpenAI's Whisper model. It allows users to upload audio files and receive transcriptions.

## Project Structure

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/Scripts/activate  # On Windows
    source venv/bin/activate      # On Unix or MacOS
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server:**
    ```sh
    uvicorn app:app --host localhost --port 8000 --reload
    ```

2. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000`.

## Endpoints

- **GET `/`**: Serves the HTML interface from `templates/index.html`.
- **POST `/transcribe/`**: Accepts multiple audio files and returns their transcriptions.

## Example Usage

1. Open the application in your browser.
2. Upload audio files using the provided interface.
3. Click the "Transcribe" button to receive the transcriptions.

## Dependencies

- FastAPI
- Whisper
- Torch
- Uvicorn

## License

This project is licensed under the MIT License.