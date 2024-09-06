import streamlit as st
import moviepy.editor as m
import tempfile

st.set_page_config(
    page_title="Pure Tune",
    page_icon="icon.png",
    menu_items={
        "About":"Pure Tune lets you effortlessly extract audio from video clips. Upload your video, and receive a high-quality audio file instantly. Perfect for content creators, music lovers, and anyone looking to separate audio from video."
    }   
)

st.write("<h2 style='color:#9DDA48;font-size:33px;'>Extract High-Quality Audio from Your Videos</h2>",unsafe_allow_html=True)

file=st.file_uploader("Upload Video",type=["mp4", "mov", "avi", "mkv"])

if file:
    with st.spinner("This may take few seconds..."):
        with tempfile.NamedTemporaryFile(delete=False,suffix=".mp4") as temp_file:
            temp_file.write(file.read())
            filename=temp_file.name

        try:
            video=m.VideoFileClip(filename)
            audio=video.audio
            audio.write_audiofile("audio.mp3")
            st.audio("audio.mp3")
            with open("audio.mp3","rb") as audio:
                st.download_button("Download",audio.read(),"audio.mp3")
        except:
            st.error("The video does not contain an audio track.")