from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    dominant_emotion = response["dominant_emotion"]
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    return f"For the given statement, the system response is 'anger':{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def loadIndex():
    return render_template('index.html')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)