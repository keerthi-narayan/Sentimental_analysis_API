# Sentiment Analysis API

This project implements a RESTful API using Flask to perform sentiment analysis on social media posts. The API leverages the Hugging Face Transformers library for language model integration and supports multiple endpoints for text analysis.

---

## Features

* **Sentiment Analysis**: Analyze text to determine its sentiment (positive, negative, or neutral).
* **Batch Processing**: Process multiple texts in a single request.
* **Text Preprocessing**: Handle emojis, URLs, and excess whitespace.
* **Health Check**: Verify API status.
* **Historical Data**: Retrieve previously processed results.

---

## Requirements

* Python 3.8+
* Flask Framework
* Hugging Face Transformers Library
* Additional Libraries: `emoji`, `re`

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [API Endpoints](#api-endpoints)
- [Text Preprocessing](#text-preprocessing)
- [Running the Application](#running-the-application)
- [Postman_Collection]_(#importing-.json-file-into-postman)
- [Testing with Postman](#testing-with-postman)
- [Running Tests](#running-tests)
- [Project Evaluation](#project-evaluation)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## API Endpoints

### 1. **Single Text Analysis**

* **Endpoint**: `/analyze`
* **Method**: POST
* **Request Body** (JSON):

  ```json
  {
      "text": "I love Python!"
  }
  ```
* **Response**:

  ```json
  {
      "text": "I love Python!",
      "preprocessed_text": "I love Python!",
      "analysis": [
          {
              "label": "POSITIVE",
              "score": 0.999
          }
      ]
  }
  ```

### 2. **Batch Text Analysis**

* **Endpoint**: `/batch`
* **Method**: POST
* **Request Body** (JSON):

  ```json
  {
      "texts": ["I love Python!", "Debugging is hard."]
  }
  ```
* **Response**:

  ```json
  [
      {
          "text": "I love Python!",
          "preprocessed_text": "I love Python!",
          "analysis": [
              {
                  "label": "POSITIVE",
                  "score": 0.999
              }
          ]
      },
      {
          "text": "Debugging is hard.",
          "preprocessed_text": "Debugging is hard.",
          "analysis": [
              {
                  "label": "NEGATIVE",
                  "score": 0.876
              }
          ]
      }
  ]
  ```

### 3. **Health Check**

* **Endpoint**: `/health`
* **Method**: GET
* **Response**:

  ```json
  {
      "status": "API is running"
  }
  ```

### 4. **Historical Results**

* **Endpoint**: `/history`
* **Method**: GET
* **Response**:

  ```json
  [
      {
          "text": "I love Python!",
          "preprocessed_text": "I love Python!",
          "analysis": [
              {
                  "label": "POSITIVE",
                  "score": 0.999
              }
          ]
      }
  ]
  ```

---

## Text Preprocessing

The preprocessing pipeline includes:

1. **Emoji Conversion**: Converts emojis to descriptive text (e.g., "🚀" becomes "\:rocket:").
2. **URL Removal**: Strips out URLs from the text.
3. **Whitespace Handling**: Removes extra spaces.

---

## Running the Application

1. Clone the repository.

   ```bash
   git clone <repository-url>
   cd SentimentAPI
   ```

2. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application.

   ```bash
   python app.py
   ```

4. The API will be available at:

   ```
   http://127.0.0.1:5000/
   ```

---

## Post man Collection 

Open Postman > Import > Upload the sentiment_analysis_api_collection.json file.

## Testing with Postman

1. Open Postman.
2. Select **POST** or **GET** based on the endpoint.
3. Enter the endpoint URL (e.g., `http://127.0.0.1:5000/analyze`).
4. For POST requests, provide a JSON body and set the `Content-Type` to `application/json`.
5. Send the request and view the response.

---

## Running Tests

1. Ensure `pytest` is installed:

   ```bash
   pip install pytest
   ```

2. Run the test suite:

   ```bash
   pytest test_app.py
   ```

3. Verify all tests pass successfully.

---

## Project Evaluation

* **Functionality** (40%): Ensure the API produces accurate sentiment analysis results.
* **API Design** (25%): Adhere to RESTful principles.
* **Code Quality** (20%): Clean and modular code structure.
* **Documentation** (15%): Comprehensive and user-friendly README.

---

## Future Enhancements

* **Real-time Twitter Analysis**: Fetch and analyze tweets in real-time.
* **Sentiment Trends Dashboard**: Visualize sentiment trends using a front-end dashboard.
* **Export Functionality**: Allow exporting results to CSV/Excel.
* **API Key Authentication**: Secure API with API keys.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
