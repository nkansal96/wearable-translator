#!/bin/bash

sudo pip2 install --upgrade watson-developer-cloud
sudo pip2 install --playsound
sudo pip2 install -U PyObjc
sudo pip2 install --upgrade google-cloud

brew install portaudio
sudo pip2 install auroraapi==0.0.10

python2 translator.py $1 $2 $3
