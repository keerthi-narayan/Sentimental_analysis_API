from flask import Flask, request, jsonify
from transformers import pipeline
import re
import emoji
import time

app = Flask(__name__)

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# In-memory storage for historical results
history = []

# Function for text preprocessing
def preprocess_text(text):
    # Convert emojis to text
    text = emoji.demojize(text)
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Middleware for performance logging
@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request_time(response):
    elapsed_time = time.time() - request.start_time
    app.logger.info(f"Processing time: {elapsed_time:.2f} seconds")
    return response

# Define route for single text analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input"}), 400
    if len(data['text']) > 280:
        return jsonify({"error": "Text exceeds character limit of 280"}), 400
    preprocessed_text = preprocess_text(data['text'])
    result = sentiment_analyzer(preprocessed_text)
    # Save to history
    history.append({"text": data['text'], "preprocessed_text": preprocessed_text, "analysis": result})
    return jsonify({"text": data['text'], "preprocessed_text": preprocessed_text, "analysis": result})

# Define route for batch text analysis
@app.route('/batch', methods=['POST'])
def batch_analyze():
    data = request.json
    if not data or 'texts' not in data:
        return jsonify({"error": "Invalid input"}), 400
    results = []
    for text in data['texts']:
        if len(text) > 280:
            results.append({"text": text, "error": "Text exceeds character limit of 280"})
            continue
        preprocessed_text = preprocess_text(text)
        analysis = sentiment_analyzer(preprocessed_text)
        # Save to history
        history.append({"text": text, "preprocessed_text": preprocessed_text, "analysis": analysis})
        results.append({"text": text, "preprocessed_text": preprocessed_text, "analysis": analysis})
    return jsonify(results)

# Define route for API health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

# Define route for historical results
@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(history), 200

# Start Flask server
if __name__ == '__main__':
    app.run(debug=True)
