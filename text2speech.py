from watson_developer_cloud import TextToSpeechV1
from playsound import playsound
import json
import utils
import sys

#language mapping
#see instructions on how to add a new language/voice
languages = {
"spanish":"es-ES_EnriqueVoice",  #default
"english":"en-US_MichaelVoice", 
"german":"de-DE_BirgitVoice", 
"french":"fr-FR_ReneeVoice",
"default":"es-ES_EnriqueVoice"
}

#Text to Speech service credentials. Refer Instructions text to see where this was retrieved from
#flag is used to break the loop and exit the program
username = 'c2f3926e-b27d-4fa1-bb90-c5b7527df00c'
password = 'Bxg3lwBI7LNb'
flag = True

#parse input arguments
if not utils.validateInputArgs(sys.argv):
	print("Invalid arguments. Expected: \npython2 text2speech.py \"language(optional)\"")
	sys.exit()

#read language from args
voice = utils.getVoice(languages, sys.argv)

#loop to iterate input
while flag:
	text = raw_input("Using " + voice + ". Enter text to convert to speech: \n")

	#validate input and proceed
	if utils.validateInput(text):
		parsedText = text.strip()
		text_to_speech = TextToSpeechV1(
			username=username,
			password=password,
			x_watson_learning_opt_out=False)# Optional flag

		print('\nConverting text to speech with IBM Watson API Text To Speech service..')
		#convert text input and save temp audio file
		with open('output.mp3', 'w+b') as audio_file:
			audio_file.write(
				text_to_speech.synthesize(parsedText, accept='audio/mp3',
				voice=voice))

		print('Conversion completed. Playing audio..')
		playsound('output.mp3')
		flag = utils.shouldContinue(raw_input('Audio played successfully. Type \'yes\' to continue \'no\' to quit: '))
	else:
		print('Input cannot be empty. Please enter a phrase or sentence for conversion')


