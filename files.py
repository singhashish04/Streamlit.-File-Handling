import streamlit as st
import pandas as pd

# Uploading CSV Files
st.subheader('Upoading the CSV files')
df = st.file_uploader('Upload the CSV file : ', type = ['csv','xlsx'])

# Loading CSV Files
st.subheader('Loading the CSV files')
df = pd.read_csv('Products.csv')        
if df is not None:
    st.table(df.head())

# Dealing with Image
st.subheader('Dealing with Image Directly')
st.image('img.png')                     

# Dealing with Image while uploading
st.subheader('Dealing with Image while uploading')
img_file = st.file_uploader('Upload the img : ', type = ['png','jpeg'])
if img_file is not None:
    st.image(img_file)

# Dealing with Audio
st.subheader('Dealing with Audio Directly')
st.audio('song.mp3')        

# Dealing with Audio while Uploading
st.subheader('Dealing with Audio while Uploading')
audio_file = st.file_uploader('Upload the Audio : ', type = ['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file)

# Working with Video
st.subheader('Working with Video')
video_file = st.file_uploader("Upload the video : ", type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file  , start_time = 0 )
