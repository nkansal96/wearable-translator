import sys

#validates the input entered at the prompt. This checks for an empty string
def validateInput(inputText):
	strippedText = inputText.strip();
	return bool(strippedText)

#check to see if iteration should continue or break. Based on yes/no response from user
def shouldContinue(inputText):
	stripAndConvertCase = inputText.strip().lower();
	return stripAndConvertCase != 'no'

#validates the number of input arguments for program execution
def validateInputArgs(args):
	return len(args) >= 1 and len(args) < 3

#returns the voice to be used for speech based on input args
def getVoice(languages, args):
	arg = args[1].strip().lower() if len(args) == 2 else 'default'
	return languages[arg] if arg in languages else languages['default']
	
