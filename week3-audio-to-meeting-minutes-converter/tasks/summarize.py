import logging
import requests
from typing import Optional
from config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def summarize(transcript: str) -> str:
    """
    Summarize the transcript into structured meeting minutes using Perplexity API.
    
    Args:
        transcript: Text to summarize
        
    Returns:
        str: Structured meeting minutes
        
    Raises:
        Exception: If summarization fails
    """
    try:
        if not settings.PERPLEXITY_API_KEY:
            logger.warning("PERPLEXITY_API_KEY not set. Returning original transcript.")
            return transcript

        logger.info("Starting summarization with Perplexity API")
        
        # Prepare the prompt with clear structure
        prompt = f"""Please convert the following meeting transcript into well-structured meeting minutes. 
        Follow this exact format:

        # Meeting Minutes

        ## Key Points
        - [List the main topics discussed]
        - [Include important decisions made]
        - [Note any significant announcements]

        ## Action Items
        - [Task 1] - [Owner] - [Deadline if mentioned]
        - [Task 2] - [Owner] - [Deadline if mentioned]

        ## Decisions Made
        - [Decision 1]
        - [Decision 2]

        ## Next Steps
        - [Next meeting date if mentioned]
        - [Follow-up actions]

        ## Additional Notes
        - [Any other relevant information]

        Here is the transcript:
        {transcript}
        """
        
        # Call Perplexity API with correct format
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            json={
                "model": "sonar-pro",
                "messages": [
                    {
                        "role": "system",
                        "content": """You are a professional meeting minutes summarizer. 
                        Your task is to create clear, concise, and well-structured meeting minutes.
                        Always follow the exact format provided in the prompt.
                        Focus on extracting actionable items, decisions, and key points.
                        If any section has no relevant information, write 'None' for that section."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 1000,
                "temperature": 0.7
            }
        )
        
        # Log response for debugging
        logger.info(f"API Response Status: {response.status_code}")
        logger.info(f"API Response Headers: {response.headers}")
        
        if response.status_code != 200:
            logger.error(f"API Error Response: {response.text}")
            return transcript
            
        result = response.json()
        
        logger.info("Summarization completed")
        return result["choices"][0]["message"]["content"]
        
    except Exception as e:
        logger.error(f"Summarization failed: {str(e)}")
        if hasattr(e, 'response'):
            logger.error(f"Error Response: {e.response.text}")
        return transcript  # Return original transcript if summarization fails