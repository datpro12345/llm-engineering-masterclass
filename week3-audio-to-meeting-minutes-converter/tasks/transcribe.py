import logging
import requests
import time
from typing import Optional
from config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transcribe(audio_bytes: bytes, model: str = "universal", language_code: Optional[str] = None) -> str:
    """
    Transcribe audio bytes to text using AssemblyAI REST API.
    
    Args:
        audio_bytes: Raw audio data in bytes
        model: Speech model to use ("universal", "whisper-1", or "nano")
        language_code: Optional language code (e.g., "vi", "en", "ja")
        
    Returns:
        str: Transcribed text
        
    Raises:
        Exception: If transcription fails
    """
    try:
        base_url = "https://api.assemblyai.com"
        headers = {
            "authorization": settings.ASSEMBLYAI_API_KEY
        }

        # Step 1: Upload audio file
        logger.info("Uploading audio file...")
        upload_response = requests.post(
            f"{base_url}/v2/upload",
            headers=headers,
            data=audio_bytes
        )
        upload_response.raise_for_status()
        audio_url = upload_response.json()["upload_url"]
        logger.info("Audio file uploaded successfully")

        # Step 2: Start transcription
        logger.info("Starting transcription...")
        data = {
            "audio_url": audio_url,
            "speech_model": model
        }
        
        # Add language code if specified
        if language_code:
            data["language_code"] = language_code
            
        transcript_response = requests.post(
            f"{base_url}/v2/transcript",
            json=data,
            headers=headers
        )
        transcript_response.raise_for_status()
        transcript_id = transcript_response.json()['id']

        # Step 3: Poll for results
        logger.info("Polling for transcription results...")
        polling_endpoint = f"{base_url}/v2/transcript/{transcript_id}"
        
        while True:
            polling_response = requests.get(polling_endpoint, headers=headers)
            polling_response.raise_for_status()
            transcription_result = polling_response.json()

            if transcription_result['status'] == 'completed':
                logger.info("Transcription completed successfully")
                return transcription_result['text']

            elif transcription_result['status'] == 'error':
                error_msg = f"Transcription failed: {transcription_result.get('error', 'Unknown error')}"
                logger.error(error_msg)
                raise RuntimeError(error_msg)

            else:
                logger.info("Transcription in progress...")
                time.sleep(3)

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Transcription failed: {str(e)}")
        raise