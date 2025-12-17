import pyttsx3
import speech_recognition as sr
import eel
import time
from engine.gesture_manager import start_gesture, stop_gesture


def speak(text):
    engine= pyttsx3.init('sapi5')
    voices=engine.getProperty("voices")
    engine.setProperty("voices",voices[0].id)
    engine.setProperty('rate',180)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


# @eel.expose
def takecommand():

    r= sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)

        audio= r.listen(source,10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing...')
        query= r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)
        # time.sleep(1)
        speak(query)
        

    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommand(message=1):


    if message==1 :
            query = takecommand()
            print (query)
            eel.senderText(query)

    else:
        query= message
        eel.senderText(query)


    try:
        

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)


        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                    
                whatsApp(contact_no, query, message, name)


        elif "turn on gesture" in query or "start gesture" in query:
            from engine.gesture_manager import start_gesture
            speak("Gesture control activated")
            start_gesture(mode=1)

        elif "turn off gesture" in query or "stop gesture" in query:
            from engine.gesture_manager import stop_gesture
            speak("Gesture control stopped")
            stop_gesture()

        elif "gesture keyboard" in query:
            from engine.gesture_manager import start_gesture
            speak("Gesture keyboard mode activated")
            start_gesture(mode=2)

        
            
        else :
            print('not run')

    except:
        print("error")


    eel.ShowHood()


    @eel.expose
    def ui_start_gesture():
        return start_gesture(mode=1)

    @eel.expose
    def ui_stop_gesture():
        return stop_gesture()