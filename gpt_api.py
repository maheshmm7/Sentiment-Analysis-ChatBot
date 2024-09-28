import requests

# Hugging Face API URL for GPT-2
API_URL_GPT = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

def query_gpt(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL_GPT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
