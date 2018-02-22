# Import the package
import auroraapi as aurora

# Set your application settings
aurora.set_app_id("f2f2bd7b9ab7450d5d7fe1fc8a09849c")       # put your app ID here
aurora.set_app_token("VN4qGg2rrO3lcJYtkBAAFaZSNkCBUf") # put your app token here

# Start listening until 1.0s of silence
#speech = aurora.Speech.listen()
# Or specify your own silence timeout (0.5 seconds shown here)
# speech = aurora.Speech.listen(silence_len=0.5)

def stt():
    "Returns the string to the "
    speech = aurora.Speech.listen(length=3)

    # Convert to text
    p = speech.text()
    return(p.text) # prints the prediction
