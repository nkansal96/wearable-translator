# Call the TTS API to convert "Hello world" to speech
speech = aurora.Text("Hello world").speech()

# Previous API returned a Speech object, so we can just call
# the text() method to get a prediction
p = speech.text()
print(p.text) # 'hello world'
