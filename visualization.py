# visualization.py
import plotly.express as px
import streamlit as st

# Updated function to plot sentiment results with human-readable labels
def plot_sentiment(results):
    # Mapping the Hugging Face labels to human-readable categories
    label_mapping = {
        "LABEL_2": "Positive",
        "LABEL_1": "Neutral",
        "LABEL_0": "Negative"
    }

    if results:
        # Map labels to human-readable labels
        labels = [label_mapping.get(res['label'], res['label']) for res in results]
        scores = [res['score'] for res in results]
        fig = px.pie(values=scores, names=labels, title='Sentiment Analysis Results')
        st.plotly_chart(fig)
    else:
        st.error("Unable to generate sentiment analysis results.")
