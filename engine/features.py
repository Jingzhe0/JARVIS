from playsound import playsound
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit


#playing assistand sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\\\assests\\\\audio\\\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)

    # playsound(r'www//assests//audio//www_assets_audio_start_sound.mp3')

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)

    else:
        speak("not found")


def PlayYouTube(query):
    search_term= extract_yt_term(query)
    speak("Playing "+search_term+ "on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    # Define regular expression to capture song name
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    # Use research to find match in command
    match= re.search(pattern,command,re.IGNORECASE)

    return match.group(1) if match else None 
