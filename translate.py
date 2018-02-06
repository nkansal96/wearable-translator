import auroraapi as aurora

# Set your application settings
aurora.set_app_id("50934cf119d9446e54cfbf8f29e66a52") # put your app ID here
aurora.set_app_token("NuQZQj2hCdd3MWV0FSutdXGR1VFPC") # put your app token here

# load a WAV file
a = aurora.audio.AudioFile.create_from_filename("test.wav")

# or open an already-open file
# with open("test.wav", "rb") as f:
#   a = aurora.audio.AudioFile.create_from_file(f)

p = aurora.Speech(a).text()
print(p.text) # 'hello world' 
