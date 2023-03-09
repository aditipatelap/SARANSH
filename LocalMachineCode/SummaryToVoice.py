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
    engine.setProperty("rate", 150)
    #  'rate' to set tempo of the speech
    #  'rest' to set rest time between two sentences.

    # convert text into voice
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------ For Testing ------
# voice(""" If you wish to create a program in Python that utilises the GPIO port on your Raspberry Pi then you'll need to install this library. The RPi.GPIO Python library allows you to easily configure and read-write the input/output pins on the GPIO header within a Python script. """)
