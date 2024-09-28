# app.py
import streamlit as st
import requests
import plotly.express as px

# Set up Hugging Face API URLs and headers
API_URL_SENTIMENT = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
headers = {"Authorization": "Bearer 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"}

# Function to perform sentiment analysis using Hugging Face API
def analyze_sentiment(text):
    response = requests.post(API_URL_SENTIMENT, headers=headers, json={"inputs": text})
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to analyze sentiment: {response.status_code}")
        return None

# Mapping of labels to human-readable format
label_mapping = {
    "LABEL_2": "Positive",
    "LABEL_1": "Neutral",
    "LABEL_0": "Negative"
}

# Function to plot sentiment results as a pie chart
def plot_sentiment_pie(results):
    if results:
        labels = [label_mapping.get(res['label'], res['label']) for res in results]
        scores = [res['score'] for res in results]
        fig = px.pie(values=scores, names=labels, title='Sentiment Analysis - Pie Chart')
        st.plotly_chart(fig)
    else:
        st.error("Unable to generate sentiment analysis results.")

# Function to plot sentiment results as a bar chart
def plot_sentiment_bar(results):
    if results:
        labels = [label_mapping.get(res['label'], res['label']) for res in results]
        scores = [res['score'] for res in results]
        fig = px.bar(x=labels, y=scores, title='Sentiment Analysis - Bar Chart', labels={'x': 'Sentiment', 'y': 'Score'})
        st.plotly_chart(fig)
    else:
        st.error("Unable to generate sentiment analysis results.")

# Function to plot sentiment results as a horizontal bar chart
def plot_sentiment_horizontal_bar(results):
    if results:
        labels = [label_mapping.get(res['label'], res['label']) for res in results]
        scores = [res['score'] for res in results]
        fig = px.bar(x=scores, y=labels, orientation='h', title='Sentiment Analysis - Horizontal Bar Chart',
                     labels={'x': 'Score', 'y': 'Sentiment'})
        st.plotly_chart(fig)
    else:
        st.error("Unable to generate sentiment analysis results.")

# Function to plot sentiment results as a donut chart
def plot_sentiment_donut(results):
    if results:
        labels = [label_mapping.get(res['label'], res['label']) for res in results]
        scores = [res['score'] for res in results]
        fig = px.pie(values=scores, names=labels, hole=0.4, title='Sentiment Analysis - Donut Chart')
        st.plotly_chart(fig)
    else:
        st.error("Unable to generate sentiment analysis results.")

# Streamlit app
st.title("Sentiment Analysis Application")
st.write("This app performs sentiment analysis on the input text and visualizes the results with multiple charts.")

# User input
user_input = st.text_area("Enter your input text:")

# Analyze sentiment when the button is clicked
if st.button("Analyze Sentiment"):
    with st.spinner("Analyzing sentiment..."):
        sentiment_result = analyze_sentiment(user_input)

    # If sentiment_result is valid, display the results
    if sentiment_result and isinstance(sentiment_result, list):
        sentiment_data = sentiment_result[0]  # Get the first list (the actual results)

        if isinstance(sentiment_data, list):
            st.write("**Sentiment Analysis Result:**")
            for result in sentiment_data:
                if 'label' in result and 'score' in result:
                    # Map the label to a human-readable format
                    human_readable_label = label_mapping.get(result['label'], "Unknown")
                    st.write(f"{human_readable_label}, Score: {result['score']:.2f}")

            # Plot all sentiment charts
            plot_sentiment_pie(sentiment_data)
            plot_sentiment_bar(sentiment_data)
            plot_sentiment_horizontal_bar(sentiment_data)
            plot_sentiment_donut(sentiment_data)
        else:
            st.error("Sentiment data is not in the expected format.")
    else:
        st.error("Failed to analyze sentiment due to API issues.")
