#Import the relevant libraries and functions
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the Flask app by the name Emotion Detector]
app = Flask("Emotion Detector")

#Define the function sent_detector
@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extracting emotions, their score and dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion_name = response['dominant_emotion']

    # Return a formatted string with the emotion detection and their score and dominant emotion
    result = f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion_name}."
    return result

#Render the HTML template using render_index_page]

@app.route("/")
def render_index_page():
    return render_template('index.html')

#Run the application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
