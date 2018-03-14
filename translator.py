# Import the package
import auroraapi as aurora
import sys

# Import from other python files
from gTranslate import translate_text
from text2speech import tts

#Collect app id and app token

if (len(sys.argv) != 5):
	language = 'es' #Make default language spanish
	print ("Must input language, app-id, token-id, and device id")
	sys.exit() 
else:
	if ((sys.argv[1] != "es") and (sys.argv[1] != "en") and (sys.argv[1] != "de") and (sys.argv[1] != "fr") and (sys.argv[1] != "it") and (sys.argv[1] != "ja") and (sys.argv[1] != "pt")):
		print ("Language parameter must be in ISO 639-1 form")
		sys.exit()

	language = sys.argv[1]
	app_id = sys.argv[2]
	app_token = sys.argv[3]
	device_id = sys.argv[4]
	# Set your application settings
	aurora.set_app_id(app_id) # put your app ID here
	aurora.set_app_token(app_token) # put your app token here
	aurora.set_device_id(device_id)



# Set your application settings
#aurora.set_app_id("f2f2bd7b9ab7450d5d7fe1fc8a09849c") # put your app ID here
#aurora.set_app_token("VN4qGg2rrO3lcJYtkBAAFaZSNkCBUf") # put your app token here

# Start listening until 1.0s of silence
# Or specify your own silence timeout



def stt():
    "Returns the string to the "
    #speech = aurora.Speech.listen(length=3)
    speech = aurora.Speech.listen(silence_len=1.0)

    # Convert to text
    output = speech.text()
    print("")
    print ("Aurora speech to text:")
    print("Detected speech: " + output.text)
    return(output.text) # prints the prediction
    
    
#Executable from now on
text = stt() #speech to text
	
tts(translate_text(text, language), language) #text to speech






