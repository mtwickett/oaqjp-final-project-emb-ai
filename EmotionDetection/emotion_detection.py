import requests


EMOTION_KEYS = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]

def _none_scores():
    return {k: None for k in EMOTION_KEYS}

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not str(text_to_analyze).strip():
        return _none_scores()

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(
        url,
        json={ "raw_document": { "text": text_to_analyze } },
        headers=headers
        )
    
    if response.status_code == 400:
        return _none_scores()
    if response.status_code != 200:
        return _none_scores()

    
    json_response = response.json()
    
    emotion_scores = json_response.get('emotionPredictions',[{}])[0].get('emotion',{})
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {**emotion_scores, "dominant_emotion": dominant_emotion}
