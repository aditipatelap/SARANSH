import CameraToText, SummaryToVoice
from gensim.summarization import summarize
import cv2
from deep_translator import GoogleTranslator
import RPi.GPIO as GPIO
import time

# Set up for switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Create object of opencv
vid = cv2.VideoCapture(0)
while(True):

    # Capture the video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    input_state = GPIO.input(18)
    
    # when user press switch
    if input_state == False:

        # save image in local drive
        cv2.imwrite("lastImage.jpg", frame)
        #text = CameraToText.textConverter("test.png")
        text = CameraToText.textConverter("lastImage.jpg")
        print("-----Text Start------")
        print(text)
        print("-----Text End------")
        # check if text empty or  not able to create summary
        if len(text.split()) != text:
            # create summary from text
            print("-----English Summary Start------")
            summary = summarize(text, ratio=0.3)
            print(summary)
            print("-----English Summary End------")
            
            
            
            translated = GoogleTranslator(source='auto', target='hi').translate(summary)
            
            print("-----Hindi Summary Start------")
            print(translated)
            print("-----Hindi Summary End------")
            # convert summary into voice
            #SummaryToVoice.voice(translated)
            SummaryToVoice.voice(summary)
        else:
            print("error")
            SummaryToVoice.voice("Adjust text photo properly")
        
            # the 'q' button is set as the
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()