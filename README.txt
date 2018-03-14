*********Important: The script requires python2.7 and Aurora 0.0.10 for successful execution**********

----PYTHON----

To run the wearable-translator application, Python 2 has to be installed. The latest version of Python 2 can be found here:

  https://www.python.org/downloads/release/python-2714/
 
Download and install the version that corresponds to the operating system you are working on.



----DEPENDANCIES----

In order to properly execute and use the wearable-translator, the appropriate dependencies have to be installed.
The following is a breakdown of which components of the translator need which dependencies. In any case, all of them have to be installed. Execute all of the commands in the terminal. In part 3 (Speech to Text), ensure you are executing the appropriate commands for the operating system you are working on.

1. Text to Speech

  a. Watson API python SDK
    command: pip install --upgrade watson-developer-cloud

  b. Audio play service
    command: pip install playsound
    command: pip install -U PyObjC


2. Text to Translated Text

  a. Google Cloud
    command: pip install --upgrade google-cloud
    
    
3. Speech to Text

  - macOS command:
    a. Port Audio 
      command: brew install portaudio
    b. Aurora API
      command: pip install auroraapi==0.0.10

  - Linux command:
    a. Port Audio
      command: sudo apt-get install python-pyaudio
    b. Aurora API
      command: pip install auroraapi==0.0.10



----CONFIGURATION----

To use the wearable-translator application, some configuration steps have to be taken to ensure all of the components that make up the application are functioning.

1. Aurora API

  To use the translator, the user needs to have an Aurora application id and token. Visit the Aurora website to purchase access to its services:
    https://dashboard.auroraapi.com/login


2. Google Translate API

  The Google API's text to text service requires service credentials for authentication which can be acquired from Google. Instructions on how to use the API can be found at Google's developers website:
    https://developers.google.com/api-client-library/python/auth/api-keys


3. IBM Watson API

  The Watson API's text to speech service requires service credentials for authentication. This has already been created for the provided account and the values are saved in the username and password variables within the script. Instructions on how to view your service credentials can be found at: 
    https://console.bluemix.net/docs/services/watson/getting-started-credentials.html#service-credentials-for-watson-services


----EXECUTION----

To execute the wearable translator, run the following command in your command line:
  python2 translator.py language app_id app_token device_id
 
Replace "language" with the ISO 639-A acronym of your desired target language.
  Supported languages:
                        Language  |  ISO 639-A Acronym
                        ------------------------------
                        English   |   en
                        Spanish   |   es
                        German    |   de
                        French    |   fr
                        Italian   |   it
                        Japansese |   ja
                        Portuguese|   pt                        
                        
Replace "app_id" with your Aurora application id.
Replace "app_token" with your Aurora application token.
Replace "device_id" with the id of the device the application is running on.

Example of a command line argument that would have the translator translate to Spanish:
  python2 translator.py es f2f2bd7b9ab7450d5d7fe1fc8a09849c VN4qGg2rrO3lcJYtkBAAFaZSNkCBUf 1234
