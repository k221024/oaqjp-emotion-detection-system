import requests  # Import the requests library to handle HTTP requests

#Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    #URL of the emotion detector analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  

    #Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    #Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    #Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotions and their score from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    #Collecting Emotions into single file
    emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}

    #Finding the dominant emotion with maximum score
    dominant_emotion_name = max(emotions, key=emotions.get)

    #Adding dominant_emotion key and value
    emotions['dominant_emotion'] = dominant_emotion_name

    return emotions
