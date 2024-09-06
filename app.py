import streamlit as st
import moviepy.editor as m
import tempfile
import os

# Streamlit page configuration
st.set_page_config(
    page_title="Pure Tune",
    page_icon="icon.png",
    menu_items={
        "About": "Pure Tune lets you effortlessly extract audio from video clips. Upload your video, and receive a high-quality audio file instantly. Perfect for content creators, music lovers, and anyone looking to separate audio from video."
    }
)

st.write("<h2 style='color:#9DDA48;font-size:33px;'>Extract High-Quality Audio from Your Videos</h2>", unsafe_allow_html=True)

# File uploader widget
file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi", "mkv"])

if file:
    with st.spinner("Processing your video..."):
        try:
            # Create a temporary file for the uploaded video
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file.write(file.read())
                temp_filename = temp_file.name

            # Load the video file with moviepy
            video = m.VideoFileClip(temp_filename)
            audio = video.audio

            # Define the path for the audio file
            audio_path = "audio.mp3"
            
            # Save the extracted audio to the audio file
            audio.write_audiofile(audio_path)

            # Provide options to play and download the audio file
            st.audio(audio_path)
            with open(audio_path, "rb") as audio_file:
                st.download_button("Download Audio", audio_file.read(), file_name="audio.mp3")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

        finally:
            # Clean up temporary files
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
            if os.path.exists(audio_path):
                os.remove(audio_path)
