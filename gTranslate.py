from google.cloud import translate
import os

# target language is by iso 639-1
def translate_text(text, target='es'):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"

    translate_client = translate.Client()

    result = translate_client.translate(text, target_language=target)

    #print (u'Text: ', result['input'])
    return ('Translation: ', result['translatedText'])
    #print (u'Detected source lang: ', result['detectedSourceLanguage'])

#example_text = "Hi there. My name is Jason."

#translate_text(example_text)