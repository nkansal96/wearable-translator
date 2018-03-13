# Import the package
import auroraapi as aurora
import sys

# Import from other python files
from gTranslate import translate_text
from text2speech import tts


# Set your application settings
aurora.set_app_id("f2f2bd7b9ab7450d5d7fe1fc8a09849c") # put your app ID here
aurora.set_app_token("VN4qGg2rrO3lcJYtkBAAFaZSNkCBUf") # put your app token here

# Start listening until 1.0s of silence
# Or specify your own silence timeout

language = ""

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

if (len(sys.argv) != 2):
	language = 'es' #Make default language spanish
else:
	language = sys.argv[1] 
	
tts(translate_text(text, language), language) #text to speech






