from playsound import playsound
import eel


#playing assistand sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\\\assests\\\\audio\\\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)

    # playsound(r'www//assests//audio//www_assets_audio_start_sound.mp3')


