# Import packages
import auroraapi as aurora
import sys

# Import from other python files
from gTranslate import translate_text
from text2speech import tts

#Collect app id, app token, and device id

if (len(sys.argv) != 5):
	language = 'es' #Make default language spanish
	print ("Must input language, app-id, token-id, and device-id")
	sys.exit() 
else:
	if ((sys.argv[1] != "es") and (sys.argv[1] != "en") and (sys.argv[1] != "de") and (sys.argv[1] != "fr") and (sys.argv[1] != "it") and (sys.argv[1] != "ja") and (sys.argv[1] != "pt")):
		print ("Language parameter must be in ISO 639-1 form")
		sys.exit()

	language = sys.argv[1]
	app_id = sys.argv[2]
	app_token = sys.argv[3]
	device_id = sys.argv[4]
	
	# Set the application settings
	aurora.set_app_id(app_id)
	aurora.set_app_token(app_token)
	aurora.set_device_id(device_id)


def stt():
    speech = aurora.Speech.listen(silence_len=1.0)

    # Convert to text
    output = speech.text()
    print("")
    print ("Aurora speech to text:")
    print("Detected speech: " + output.text)
    return(output.text) # returns the prediction
    
    
text = stt() #speech to text
tts(translate_text(text, language), language) #text to speech
