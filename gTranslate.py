from google.cloud import translate
import os
import six

# target language is by iso 639-1
def translate_text(text, target='es'):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
    	text = text.decode('utf-8')


    result = translate_client.translate(text, target_language=target)

    #print (u'Text: ', result['input'])
    #output = ('Translation: ', result['translatedText'])
    
    print ("")
    print ("Google Translate English text to Spanish text:")
    print (u'Translation: {}'.format(result['translatedText']))
    print (u'Detected source lang: {}'.format(result['detectedSourceLanguage']))
    return (u'{}'.format(result['translatedText']))
