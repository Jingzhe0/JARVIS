import os 
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize


def start():
        
        eel.init("www")

        playAssistantSound()
        @eel.expose
        def init():
                eel.hideLoader()
                speak("Ready for Face Authentication")
                flag= recoganize.AuthenticateFace()
                if flag==1:
                        eel.hideFaceAuth()
                        speak("Face authentication succesful")
                        eel.hideFaceAuthSuccess()
                        eel.hideStart()
                else:
                        speak("Face authentication succesful")

        os.system('start msedge.exe --app="http://localhost:8000/index.html"')

        eel.start('index.html', mode=None, host='localhost', block=True)

