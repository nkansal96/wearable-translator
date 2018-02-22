import text2speech
from gTranslate import translate_text
import sys
import subprocess
from watson_developer_cloud import TextToSpeechV1

from sttR import stt

def wearable_translator(target='es'):
    #Shadi stuff
    print ("came here")
    text = stt()
    translated = translate_text(text, target)
    ret = t2s.utils.getVoice(target, translated)
    print (ret)
