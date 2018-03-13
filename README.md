*********Important: The script requires python2.7 and Aurora 0.0.10 for successful execution**********

installing python2 for Ubuntu:
http://docs.python-guide.org/en/latest/starting/install2/linux/

installing python2 for MAC: 
http://docs.python-guide.org/en/latest/starting/install2/osx/


----DEPENDANCIES---- (execute the provided commands in the terminal)

Text to Speech
a. Watson API python SDK
command: pip install --upgrade watson-developer-cloud

b. Audio play service
command: pip install playsound
command: pip install -U PyObjC

2. Google Cloud 
command: pip install --upgrade google-cloud

3. Speech to Text

macOS command: 
a. brew install portaudio
b. pip install auroraapi==0.0.10

Linux command:
a. sudo apt-get install python-pyaudio
b. pip install auroraapi==0.0.10

----CONFIGURATION----

Aurora's API's speech to text service requires a token and ID that were provided to us by the owner. 

The Google API's text to text service requires service credentials for authentication. Instructions on how to create a key is given in the below link:
https://developers.google.com/api-client-library/python/auth/api-keys

The Watson API's text to speech service requires service credentials for authentication. This has already been created for the provided account and the values are saved in the username and password variables within the script. 

Instructions on how to view your service credentials can be found at: 
https://console.bluemix.net/docs/services/watson/getting-started-credentials.html#service-credentials-for-watson-services


----EXECUTION----

The script for text2speech can be executed from the command line like so:

python text2speech.py language(optional)

This will give a prompt to enter the sentence you wish to convert to speech. Type the sentence and press enter. The audio will be played once the conversion is complete. At the next prompt, type 'yes' to continue or 'no' to exit the script.

The language is optional and if not specified the default spanish voice is used. You can change or add new voices by editing the languages object in the script.List of voices available:

de-DE_BirgitVoice
de-DE_DieterVoice
en-GB_KateVoice
en-US_AllisonVoice
en-US_LisaVoice
en-US_MichaelVoice
es-ES_LauraVoice
es-ES_EnriqueVoice
es-LA_SofiaVoice
es-US_SofiaVoice
fr-FR_ReneeVoice
it-IT_FrancescaVoice
ja-JP_EmiVoice
pt-BR_IsabelaVoice
obtained from: https://www.ibm.com/watson/developercloud/text-to-speech/api/v1/?node#get_voice

example: to add pt-BR_IsabelaVoice from the above list, simply specify a key value pair in the languages object within the text2speech.py script.

languages = {
"spanish":"es-ES_EnriqueVoice",  #default
"english":"en-US_MichaelVoice", 
"german":"de-DE_BirgitVoice", 
"french":"fr-FR_ReneeVoice",
"default":"es-ES_EnriqueVoice",
"newVoice": "pt-BR_IsabelaVoice"
}

to use this voice: python text2speech.py newVoice


The script for translator can be executed from the command line like so:

python translator.py language(optional)



