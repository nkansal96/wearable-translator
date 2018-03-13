#!/bin/bash

pip2 install --upgrade watson-developer-cloud
pip2 install --playsound
pip2 install -U PyObjc
pip2 install --upgrade google-cloud

brew install portaudio
pip2 install auroraapi==0.0.10

python2 translator.py $1 $2 $3
