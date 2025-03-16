# Audio to Meeting Minutes Converter

This project uses both frontier (OpenAI Whisper) and open-source (Llama 3.1) models to convert meeting audio recordings into structured meeting minutes with summaries, discussion points, and action items.

## Features

- Transcribe meeting audio recordings using OpenAI's Whisper model
- Generate structured meeting minutes using Llama 3.1
- Format output in Markdown with proper sections
- Simple Gradio UI for easy use
- Google Drive integration for reading audio files

## Technologies Used

- OpenAI Whisper for speech-to-text
- Llama 3.1 8B Instruct for text summarization
- Hugging Face Transformers for model access
- Bits & Bytes for model quantization
- Gradio for the user interface
