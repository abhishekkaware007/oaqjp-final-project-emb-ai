# Final Project

## Emotion Detection Using Watson NLP

Final Project for the Coursera course **"Developing AI Applications with Python and Flask"**.

## Project Overview
This project builds an AI-based web application that detects emotions from user input using IBM Watson NLP. It extracts scores for five primary emotions—**anger**, **disgust**, **fear**, **joy**, and **sadness**—and identifies the **dominant emotion**.

The application is packaged as a reusable Python package (`EmotionDetection`), tested with Python's built-in `unittest` framework, styled with PEP 8 standards (achieving a **10.00/10** Pylint rating), and deployed as an interactive web service using **Flask**.

---

## Directory Structure
```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py               # Package initialization exposing emotion_detector
│   └── emotion_detection.py      # Core Watson NLP request, parsing, and error handling
├── static/
│   └── mywebscript.js            # Client-side AJAX handler for web UI
├── templates/
│   └── index.html                # Frontend web interface
├── emotion_detection.py          # Standalone emotion detector script (Task 2)
├── test_emotion_detection.py     # Unit test suite verifying dominant emotions
├── server.py                     # Flask web server with error handling & routes
├── README.md                     # Project documentation
└── .gitignore                    # Git ignore file for environment and caches
```

---

## Features
1. **Watson NLP Emotion Detection:** Connects to Watson NLP `EmotionPredict` service using HTTP POST requests.
2. **Output Formatting:** Returns formatted dictionary containing scores for `anger`, `disgust`, `fear`, `joy`, and `sadness`, along with the `dominant_emotion`.
3. **Robust Error Handling:** Detects blank or invalid input (HTTP status code `400`) and returns `None` for all emotion scores, triggering an `"Invalid text! Please try again!"` alert on the frontend.
4. **Unit Testing:** Comprehensive test coverage using `unittest` for key emotional statements.
5. **Static Code Analysis:** `server.py` adheres to strict PEP 8 compliance, rated **10.00/10** on `pylint`.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhishekkaware007/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install requests flask pylint
   ```

---

## Running the Application

1. **Start the Flask server:**
   ```bash
   python3 server.py
   ```
2. **Access the application:**
   Open your browser and navigate to `http://localhost:5000` (or the corresponding Skills Network port `5000`).

---

## Running Tests & Code Quality Checks

- **Run unit tests:**
  ```bash
  python3 test_emotion_detection.py
  ```

- **Run Pylint static code analysis:**
  ```bash
  pylint server.py
  ```
