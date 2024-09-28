import requests

# Hugging Face API URL for sentiment analysis
API_URL_SENTIMENT = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
headers = {"Authorization": "Bearer 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"}

def analyze_sentiment(text):
    response = requests.post(API_URL_SENTIMENT, headers=headers, json={"inputs": text})
    response.raise_for_status()
    return response.json()
