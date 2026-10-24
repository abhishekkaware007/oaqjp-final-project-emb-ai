"""
Flask server for Emotion Detection web application.
Handles routing for text analysis requests and renders the HTML interface.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Receives text from HTML interface via GET parameters,
    calls emotion_detector, and returns the formatted response
    or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to emotion_detector
    response = emotion_detector(text_to_analyze)

    # Extract dominant emotion for validation
    dominant_emotion = response.get('dominant_emotion')

    # Error handling for invalid/blank input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format successful response
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main application index.html page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
