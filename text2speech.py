from watson_developer_cloud import TextToSpeechV1
from playsound import playsound
import json
import utils
import sys


def tts(text, lang):

	#language mapping based on ISO 639-1
	#see instructions on how to add a new language/voice
	languages = {
	"es":"es-ES_EnriqueVoice",  #default
	"en":"en-US_MichaelVoice", 
	"de":"de-DE_BirgitVoice", 
	"fr":"fr-FR_ReneeVoice",
	"it":"it-IT_FrancescaVoice",
	"ja":"ja-JP_EmiVoice",
	"pt":"pt-BR_IsabelaVoice",
	"default":"es-ES_EnriqueVoice"
	}
	
	

	#Text to Speech service credentials
	#flag is used to break the loop and exit the program
	username = 'c2f3926e-b27d-4fa1-bb90-c5b7527df00c'
	password = 'Bxg3lwBI7LNb'
	flag = True

	#parse input arguments
	if not utils.validateInputArgs(sys.argv[1]): 
	#CHANGE MADE HERE: sys.argv --> sys.argv[1]
		print("Invalid arguments. Expected: \npython2 text2speech.py \"language(optional)\"")
		sys.exit()
	
	#get voice and lanugage from 2nd parameter argument
	voice = languages[lang]
	

	#loop to iterate input
	while flag:
		#validate input and proceed
		if utils.validateInput(text):
			parsedText = text.strip()
			text_to_speech = TextToSpeechV1(
				username=username,
				password=password,
				x_watson_learning_opt_out=False)
				# Optional flag
				
			#convert text input and save temp audio file
			with open('output.mp3', 'w+b') as audio_file:
				audio_file.write(
					text_to_speech.synthesize(parsedText, accept='audio/mp3', voice=voice))

			print('Conversion completed. Playing audio..')
			playsound('output.mp3')
			flag = 0
		else:
			print('Input cannot be empty. Please enter a phrase or sentence for conversion')
			break
			

