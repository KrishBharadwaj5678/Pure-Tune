import streamlit as st
import moviepy.editor as m
import io

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
            # Read the uploaded file into memory
            video_bytes = file.read()
            video_stream = io.BytesIO(video_bytes)

            # Create a temporary file to save the video stream
            with open("temp_video.mp4", "wb") as temp_file:
                temp_file.write(video_bytes)
            
            # Load the video file with moviepy from the saved temporary file
            video = m.VideoFileClip("temp_video.mp4")
            audio = video.audio

            # Save the extracted audio to an in-memory stream
            audio_stream = io.BytesIO()
            audio.write_audiofile("temp_audio.mp3")
            audio_stream.seek(0)  # Reset stream position to the beginning

            # Provide options to play and download the audio file
            st.audio("temp_video.mp4", format="audio/mp3")
            st.download_button("Download Audio", audio_stream, file_name="audio.mp3")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
