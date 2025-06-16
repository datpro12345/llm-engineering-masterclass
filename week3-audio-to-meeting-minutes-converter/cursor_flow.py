import streamlit as st
from tasks.upload_audio import upload_audio
from tasks.transcribe import transcribe
from tasks.summarize import summarize

def main():
    st.title("Voice-to-Text Meeting Minutes")
    
    # Add model selection
    model_options = {
        "Universal (Best Quality)": "universal",
        "Whisper-1 (Balanced)": "whisper-1",
        "Nano (Fastest)": "nano"
    }
    selected_model = st.selectbox(
        "Select Speech Model",
        options=list(model_options.keys()),
        index=0  # Default to Universal
    )
    
    # Add language selection
    language_options = {
        "Auto Detect": None,
        "Vietnamese": "vi",
        "English": "en",
        "Japanese": "ja",
        "Korean": "ko",
        "Chinese": "zh"
    }
    selected_language = st.selectbox(
        "Select Language",
        options=list(language_options.keys()),
        index=0  # Default to Auto Detect
    )
    
    # File uploader
    uploaded_file = st.file_uploader("Upload Audio File", type=['mp3', 'wav', 'm4a'])
    
    if uploaded_file:
        # Show progress
        with st.spinner('Processing...'):
            # Process audio
            audio = upload_audio(file_path=uploaded_file)
            
            # Transcribe with selected options
            transcript = transcribe(
                audio_bytes=audio,
                model=model_options[selected_model],
                language_code=language_options[selected_language]
            )
            st.subheader("Transcript")
            st.write(transcript)
            
            # Generate minutes
            minutes = summarize(transcript=transcript)
            st.subheader("Meeting Minutes")
            st.write(minutes)

if __name__ == "__main__":
    main()