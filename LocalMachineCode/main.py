import CameraToText, TextToSummary, SummaryToVoice
import cv2

vid = cv2.VideoCapture(0)

while(True):

    # Capture the video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        cv2.imwrite("lastImage.jpg", frame)
        text = CameraToText.textConverter("lastImage.jpg")
        if text != "":
            summary = TextToSummary.summrizer(text)
            print(summary)
            SummaryToVoice.voice(summary)
        else:
            print("error")
            SummaryToVoice.voice("Adjust text photo properly")

    # the 'q' button is set as the
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()
