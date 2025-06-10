import logging
from typing import Union
from streamlit.runtime.uploaded_file_manager import UploadedFile

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def upload_audio(file_path: Union[str, UploadedFile]) -> bytes:
    """
    Upload and read audio file content.
    
    Args:
        file_path: Either a string path to file or Streamlit UploadedFile object
        
    Returns:
        bytes: Audio file content
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        if hasattr(file_path, 'read'):
            # If it's a Streamlit UploadedFile
            logger.info("Processing Streamlit UploadedFile")
            return file_path.read()
        else:
            # If it's a string path
            logger.info(f"Reading file from path: {file_path}")
            with open(file_path, "rb") as f:
                return f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except IOError as e:
        logger.error(f"Error reading file: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise
