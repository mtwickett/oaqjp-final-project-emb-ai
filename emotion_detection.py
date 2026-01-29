import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(
        url,
        json={ "raw_document": { "text": text_to_analyze } },
        headers=headers
        )
    
    json_response = response.json()
    
    emotion_scores = json_response.get('emotionPredictions',[{}])[0].get('emotion',{})
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {**emotion_scores, "dominant_emotion": dominant_emotion}


print(emotion_detector('I am so happy I am doing this.'))