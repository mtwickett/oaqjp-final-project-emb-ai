from flask import Flask, render_template, request
import json

from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def run_sentiment_analysis():
    text_to_analyze = request.args.get("textToAnalyze")

    emotion_scores = emotion_detector(text_to_analyze)

    if emotion_scores.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
    "For the given statement, the system response is "
    f"'anger': {emotion_scores['anger']}, "
    f"'disgust': {emotion_scores['disgust']}, "
    f"'fear': {emotion_scores['fear']}, "
    f"'joy': {emotion_scores['joy']} and "
    f"'sadness': {emotion_scores['sadness']}. "
    f"The dominant emotion is {emotion_scores['dominant_emotion']}."
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)