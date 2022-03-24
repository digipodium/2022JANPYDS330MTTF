import streamlit as st
from textblob import TextBlob
import os

def savetoUpload(file):
    file_name = file.name
    file_path = './uploads/' + file_name
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    with open(file_path, 'wb') as f:
        f.write(file.getbuffer())
        st.balloons()

def read_text(path):
    with open(path, 'r') as f:
        return TextBlob(f.read())

st.title("book NLP analysis")

file = st.file_uploader("Upload a file", type=["txt"])
if file:
    savetoUpload(file)
    blob = read_text('./uploads/'+ file.name)   
    word_count = len(blob.words)
    sentence_count = len(blob.sentences)
    st.markdown(f'''
    ---
    #### Total words: {word_count}
    #### Total sentences: {sentence_count}
    ---
    ''')
