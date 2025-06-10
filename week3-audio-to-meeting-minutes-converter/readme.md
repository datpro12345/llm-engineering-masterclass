# Audio to Meeting Minutes Converter

Convert audio recordings of meetings into structured meeting minutes using AI.

## Features

- Upload audio files (MP3, WAV)
- Automatic transcription using AssemblyAI
- AI-powered meeting minutes generation using Perplexity API
- Structured output with key points, action items, and decisions

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd week3-audio-to-meeting-minutes-converter
```

2. Create and activate conda environment:
```bash
conda env create -f environment.yml
conda activate v2tmt
```

3. Create `.env` file with your API keys:
```
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
PERPLEXITY_API_KEY=your_perplexity_api_key
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run cursor_flow.py
```

2. Open your browser at http://localhost:8501

3. Upload an audio file and wait for processing

## Project Structure

```
week3-audio-to-meeting-minutes-converter/
├── tasks/
│   ├── upload_audio.py    # Audio file handling
│   ├── transcribe.py      # AssemblyAI transcription
│   └── summarize.py       # Perplexity API summarization
├── config.py              # Configuration and settings
├── cursor_flow.py         # Main Streamlit app
└── environment.yml        # Conda environment
```

## Requirements

- Python 3.10
- AssemblyAI API key
- Perplexity API key
- See environment.yml for full dependencies