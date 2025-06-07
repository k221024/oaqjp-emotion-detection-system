"""Flask app for Emotion Detection"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint that receives text input via GET parameter,
    analyzes emotions using emotion_detector function,
    and returns the result or appropriate message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Check for blank input
    response = emotion_detector(text_to_analyze)
    if response == "Blank":
        return "Please write something."

    # Check for invalid input
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    # Extract scores and dominant emotion
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Format and return the result
    result = (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )
    return result

@app.route("/")
def render_index_page():
    """
    Render the index HTML page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
