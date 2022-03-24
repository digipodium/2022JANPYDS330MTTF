###
# streamlit run nlp\sentiapp.py
###
from textblob import TextBlob
import streamlit as st
import pandas as pd
import plotly.express as px

def analyse(text=""):
    results = []
    blob = TextBlob(text)
    for sentence in blob.sentences:
        out = get_sentiment(sentence.sentiment.polarity)
        results.append({
            'sentence': sentence.string,
            'sentiment': out,
            'polarity': sentence.sentiment.polarity
    })
    return pd.DataFrame(results)

def get_sentiment(score):
    if score > 0 and score <= 0.5:
        return 'Slighly Positive'
    elif score > 0.5 and score <= 1:
        return 'Positive'
    elif score >= -0.5 and score < 0:
        return 'Slightly Negative'
    elif score > -1 and score < -0.5:
        return 'Negative'
    else:
        return 'neutral'

st.title("Sentiment Analysis")

st.sidebar.header("User input area")

f = st.sidebar.form("userform")
content = f.text_area("Enter your text", height=250,placeholder="Enter your text for sentiment analysis here")
btn = f.form_submit_button("Submit")

if btn and content:
    results = analyse(content)
    st.sidebar.write(results)
    st.subheader("Sentiment Analysis")
    sentiment =results.sentiment.value_counts().reset_index()
    fig = px.pie(sentiment, values=sentiment['sentiment'], names=sentiment['index'], title="Sentiment Analysis")
    st.plotly_chart(fig)


