from google.cloud import translate

# target language is by iso 639-1
def translate_text(text, target='es'):

    translate_client = translate.Client()

    result = translate_client.translate(text, target_language=target)

    print (u'Text: ', result['input'])
    print (u'Translation: ', result['translatedText'])
    print (u'Detected source lang: ', result['detectedSourceLanguage'])

example_text = "Hi there. My name is Jason."

translate_text(example_text)
