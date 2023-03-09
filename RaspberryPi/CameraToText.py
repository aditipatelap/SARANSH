from PIL import Image
import pytesseract


# create method to convert image text into variable
def textConverter(image):
    # open image 
    image = Image.open(image)
    # get text from image
    text = pytesseract.image_to_string(image, lang='eng')
    return text


# ------ For Testing ------
# txt = textConverter("RaspberryPi/noText.jpg")
# txt = textConverter("RaspberryPi/test1.png")
# print(txt)
