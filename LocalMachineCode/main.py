import CameraToText, TextToSummary, SummaryToVoice
import cv2
from deep_translator import GoogleTranslator


# Create object of opencv
vid = cv2.VideoCapture(0)

# if double click detect then this function will called
def doubleClick(event, x, y, flags, param):

    # in this function five arguments are fix.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # save image in local drive
        cv2.imwrite("lastImage.jpg", frame)

        # extract text from the image
        # text = CameraToText.textConverter("LocalMachineCode/noText.jpg")
        # text = CameraToText.textConverter("LocalMachineCode/test1.png")
        text = CameraToText.textConverter("LocalMachineCode/lastImage.jpg")

        # check- if text is not empty then it will able to create summary
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
            SummaryToVoice.voice(summary) # English summary

            SummaryToVoice.voice("Hindi Summary")
            SummaryToVoice.voice(translated) # Hindi summary
            
        # if text not detected - text is empty string
        else:
            print("error")
            SummaryToVoice.voice("Adjust text photo properly.")

while True:

    # Capture the video from the camera
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('SARANSH', frame)

    # continuously check for double click event
    # when double click mouse is happened, it will process for summary
    cv2.setMouseCallback('SARANSH', doubleClick)
    
    # continuously check for 'ESC' key pressing event
    # close the program when 'ESC' key pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

vid.release()

cv2.destroyAllWindows()
