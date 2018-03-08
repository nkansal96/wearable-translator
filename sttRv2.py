# Import the package
import auroraapi as aurora

# GoogleTranslate packages
from gTranslate import translate_text

from text2speech import tts


# Set your application settings
aurora.set_app_id("f2f2bd7b9ab7450d5d7fe1fc8a09849c")       # put your app ID here
aurora.set_app_token("VN4qGg2rrO3lcJYtkBAAFaZSNkCBUf") # put your app token here

# Start listening until 1.0s of silence
#speech = aurora.Speech.listen()
# Or specify your own silence timeout (0.5 seconds shown here)
# speech = aurora.Speech.listen(silence_len=0.5)

def stt():
    "Returns the string to the "
    #speech = aurora.Speech.listen(length=3)
    speech = aurora.Speech.listen(silence_len=1.0s;)

    # Convert to text
    p = speech.text()
    print("")
    print ("Aurora speech to text:")
    print("Detected speech: " + p.text)
    return(p.text) # prints the prediction

# Translates Text to Text 
text = stt()

# Outputs the translated text
tts(translate_text(text))
