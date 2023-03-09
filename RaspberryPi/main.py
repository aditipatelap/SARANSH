import CameraToText, TextToSummary, SummaryToVoice
import cv2
from deep_translator import GoogleTranslator
import RPi.GPIO as GPIO

Set up for switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Create object of opencv
vid = cv2.VideoCapture(0)

while True:

    # Capture the video from the camera
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('SARANSH', frame)

    # input_state = GPIO.input(18)
    
    # when user press switch
    if input_state == False:

        # save image in local drive
        cv2.imwrite("lastImage.jpg", frame)

        # extract text from the image
        # text = CameraToText.textConverter("RaspberryPi/noText.jpg")
        # text = CameraToText.textConverter("RaspberryPi/test1.png")
        text = CameraToText.textConverter("RaspberryPi/lastImage.jpg")

        # print text string
        print("--------- Text Start ---------")
        print(text)
        print("--------- Text End ---------")

        # check-if text is not empty then it will be able to create summary
        if text != "":
            # print text string
            print("--------- Text Start ---------")
            print(text)
            print("--------- Text End ---------")

            # create summary from text
            summary = TextToSummary.summaryMaker(text)

            # print summary string
            print("------ English Summary Start ------")
            print(summary)
            print("----- English Summary End ------")

            # Translate summary into Hindi
            translated = GoogleTranslator(source='auto', target='hi').translate(summary)

            # print translated summary
            print("------ Hindi Summary Start ------")
            print(translated)
            print("----- Hindi Summary End ------")

            # convert summary into voice
            SummaryToVoice.voice("English Summary")
            SummaryToVoice.voice(summary)  # English summary

            SummaryToVoice.voice("Hindi Summary")
            SummaryToVoice.voice(translated)  # Hindi summary

        # if text not detected - text is empty string
        else:
            print("error")
            SummaryToVoice.voice("Adjust text photo properly.")

    # the 'q' button is set as the
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()
