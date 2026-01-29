from flask import Flask, render_template, request
import json

from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_endpoint():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_scores = emotion_detector(text_to_analyze)
    return (
        f'For the given statement, the system response is \
        {emotion_scores['anger']}, \
        {emotion_scores['disgust']}, \
        {emotion_scores['fear']}, \
        {emotion_scores['joy']} and \
        {emotion_scores['sadness']}. \
        The dominant emotion is {emotion_scores['dominant_emotion']}.'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)