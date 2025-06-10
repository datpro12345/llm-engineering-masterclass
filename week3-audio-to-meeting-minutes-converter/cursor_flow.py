import streamlit as st
from tasks.upload_audio import upload_audio
from tasks.transcribe import transcribe
from tasks.summarize import summarize

def main():
    st.title("Voice-to-Text Meeting Minutes")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload Audio File", type=['mp3', 'wav'])
    
    if uploaded_file:
        # Show progress
        with st.spinner('Processing...'):
            # Process audio
            audio = upload_audio(file_path=uploaded_file)
            
            # Transcribe
            transcript = transcribe(audio_bytes=audio)
            st.subheader("Transcript")
            st.write(transcript)
            
            # Generate minutes
            minutes = summarize(transcript=transcript)
            st.subheader("Meeting Minutes")
            st.write(minutes)

if __name__ == "__main__":
    main()