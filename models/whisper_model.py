from faster_whisper import WhisperModel
import torch

model_size = "tiny"
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model  = WhisperModel(model_size, device=device)


print(f"Using device: {device if device != 'cuda' else torch.cuda.get_device_name(0)}")

async def transcribe_audio(audio_file_path):
    segments, _ = whisper_model.transcribe(audio_file_path, beam_size=10) # Only Detect language
    full_text = ""
    for segment in segments:
        full_text += segment.text + " "
    return full_text