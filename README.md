# Sentiment Analysis Application

## Project Overview

This project is a Sentiment Analysis Application developed as part of an internship assignment for Aspireit. The application allows users to input text, analyzes the sentiment of the input using a pre-trained model, and visualizes the results through various charts.

## Features

- User-friendly interface for text input
- Sentiment analysis using the Hugging Face API
- Multiple visualizations of sentiment analysis results:
  - Pie chart
  - Bar chart
  - Horizontal bar chart
  - Donut chart
- Integration with GPT-2 for text generation (not implemented in the current version)

## Technologies Used

- Python 3.8+
- Streamlit
- Plotly
- Hugging Face API
- Requests library

## Project Structure

```
|-- your_project_folder/
    |-- app.py              # Main Streamlit app to interact with the user and visualize results
    |-- gpt_api.py          # Handles the GPT-2 text generation API calls
    |-- visualization.py    # Contains functions to visualize sentiment analysis results
    |-- README.md           # This documentation file
    |-- requirements.txt    # Dependencies for the project
```

## Setup and Installation

### Creating a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project. Here's how you can set it up:

1. Make sure you have Python 3.8 or newer installed on your system.

2. Install virtualenv if you haven't already:
   ```
   pip install virtualenv
   ```

3. Navigate to your project directory:
   ```
   git clone https://github.com/maheshmm7/Sentiment-Analysis-ChatBot.git
   ```

4. Create a new virtual environment:
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

### Installing Dependencies

Once your virtual environment is activated, you can install the project dependencies:

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Setting Up the Project

1. Clone the repository (if you haven't already):
   ```
   git clone https://github.com/maheshmm7/Sentiment-Analysis-ChatBot.git
   ```

2. Set up your Hugging Face API key:
   - Sign up for a Hugging Face account and obtain an API key
   - Replace the `headers` variable in `app.py` with your API key:
     ```python
     headers = {"Authorization": "Bearer YOUR_API_KEY_HERE"}
     ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## API Endpoints

The application uses the following Hugging Face API endpoints:

1. Sentiment Analysis API:
   - URL: `https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment`
   - Method: POST
   - Headers: `{"Authorization": "Bearer YOUR_API_KEY_HERE"}`
   - Body: `{"inputs": "Your text here"}`

2. GPT-2 Text Generation API (not currently implemented in the main app):
   - URL: `https://api-inference.huggingface.co/models/openai-community/gpt2`
   - Method: POST
   - Headers: `{"Authorization": "Bearer YOUR_API_KEY_HERE"}`
   - Body: `{"inputs": "Your prompt here"}`

## Application Flow

1. User Input:
   - The user enters text into the Streamlit interface.

2. Sentiment Analysis:
   - The input text is sent to the Hugging Face Sentiment Analysis API.
   - The API returns sentiment scores for positive, neutral, and negative sentiments.

3. Data Processing:
   - The application processes the API response, extracting sentiment labels and scores.

4. Visualization:
   - The processed data is used to create various charts (pie, bar, horizontal bar, and donut) using Plotly.

5. Display Results:
   - The Streamlit interface displays the sentiment analysis results and visualizations to the user.

## Example Usage

1. Ensure your virtual environment is activated.

2. Launch the application:
   ```
   streamlit run app.py
   ```

3. In the text area, enter a sentence or paragraph to analyze. For example:
   ```
   I absolutely love this new restaurant! The food is delicious and the service is excellent.
   ```

4. Click the "Analyze Sentiment" button.

5. View the results:
   - You'll see the sentiment scores displayed as text.
   - Below the text, you'll find four different charts visualizing the sentiment distribution.

6. Try different inputs to see how the sentiment analysis changes:
   ```
   The weather today is quite gloomy and it's making me feel a bit down.
   ```
   
   ```
   I'm not sure how I feel about this movie. It had some good parts, but also some boring scenes.
   ```

## Future Improvements

- Implement GPT-2 text generation functionality
- Add more advanced NLP features
- Improve error handling and user feedback
- Optimize performance for larger text inputs

## Author

- RANGALA MAHESH
- maheshrangala7@gmail.com
- +919032017670

## Acknowledgments

- Hugging Face for providing the sentiment analysis model
- Streamlit and Plotly for the interactive web interface and visualizations
