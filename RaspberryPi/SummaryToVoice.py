import pyttsx3

# create voice method to convert text into voice
def voice(text):
    # create object of pyttsx3
    engine = pyttsx3.init()

    # change voice language into english 
    for voice in engine.getProperty('voices'):
        if voice == 'hindi':
            engine.setProperty('voice', voice.id)
    
    # slow the patch of voice
    engine.setProperty("rest", 100)        
    # convert text into voice
    engine.say(text)
    engine.runAndWait()
    engine.stop()