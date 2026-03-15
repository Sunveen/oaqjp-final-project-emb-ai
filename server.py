"""
Application to detect emotion from the provided text
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    """
    Route to return emotion using Watson AI
    """
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    dominant_emotion = response["dominant_emotion"]
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    return (
    f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
    f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}."
)

@app.route("/")
def load_index():
    """
    Route to return index file
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
