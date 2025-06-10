import streamlit as st
from cursor_flow import meeting_minutes_flow

st.title("🗣️ Voice-to-Text Meeting Minutes")

audio_file = st.file_uploader("Upload audio (mp3/wav)", type=["mp3","wav"])
if audio_file:
    path = f"/tmp/{audio_file.name}"
    with open(path, "wb") as f: f.write(audio_file.getbuffer())
    with st.spinner("Processing..."):
        out = meeting_minutes_flow(file_path=path)
    st.header("Transcript")
    st.text_area("", out["transcript"], height=200)
    st.header("Meeting Minutes")
    st.text_area("", out["minutes"], height=200)
