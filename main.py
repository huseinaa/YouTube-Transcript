import streamlit as st
from SimplerLLM.tools.youtube import get_youtube_transcript

# App title
st.title("🎥 Mona's YouTube Transcript Extractor")

# Instructions
st.write("Enter the URL of a YouTube video to extract its transcript.")

# Input field for the YouTube video URL
video_url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=example")

# Button to extract the transcript
if st.button("Get Transcript"):
    if video_url:
        try:
            # Fetch the transcript using the SimplerLLM library
            with st.spinner("Fetching transcript..."):
                video_transcript = get_youtube_transcript(video_url)
            
            # Display the transcript with editing and copy functionality
            st.subheader("Transcript")
            edited_transcript = st.text_area("Edit Transcript", value=video_transcript, height=300)
            st.download_button("Copy Transcript", edited_transcript, file_name="transcript.txt")
        except Exception as e:
            # Handle errors
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube video URL.")

# Footer
st.write("\n\nMade with ❤️")