import pyttsx3
import speech_recognition as sr
import os


def text_voice(text):
    # init function to get an engine instance for the speech synthesis 
    engine = pyttsx3.init()
    # To set voice 0 for men and 1 for women
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    # To set speed
    rate =engine.getProperty('rate')
    engine.setProperty('rate',150)
    # say method on the engine that passing input text to be spoken
    os.system('cls')
    print('Listen Carefully......')
    engine.say(text)

    # run and wait method, it processes the voice commands. 
    engine.runAndWait()

def voice_text():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
            return("Text: "+r.recognize_google(audio_text))
        except:
            return("Sorry, I did not get that")

# a=voice_text()
# a='aaaah aaah aaah aaah aaah aaah aaah aaah aaah aah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah aaaaaaaaaahhhhhhhhhhhhh oh my god oh my god oooohhhhhhhhh gooooooooooooooooooood oh baby fuck me carefully'
# a = 'oh you sister fucking machine dick fucking ass licking whore mama having ass bitch'
a = 'aaaaaaaaahhhh baby fuck me please fuck me fuck me fuck me fuck me fuck me fuck me oooohhhhhhh myyyyyyy gooooooodd please daddy fuck me in my tiny asshole pappi fuck me fuck me fuck me fuck me'
print(voice_text())
