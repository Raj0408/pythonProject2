
# import googletrans
import pytesseract
from PIL import Image
import pyttsx3
from deep_translator import GoogleTranslator
# from googletrans import Translator


img = Image.open('image/img_3.png')


print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = "C:/Users/Raj Kaneriya/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    a = result
    print(result)

#
# j = googletrans.Translator()
# # translates the text into german language
# k = j.translate(result, dest='german')

# translator = Translator()
# translated_text = translator.translate('Hi, how are you?', dest='spanish')
# print(translated_text)
#
# translated = GoogleTranslator(source='auto', target='english').translate_file('abc.txt')
# print(translated)

# # # print(k)

# text to speech code
engine = pyttsx3.init()
engine.setProperty("rate", 130)
# an audio will be played which spea+ks the test if pyttsx3 recognizes it
engine.say(result)
engine.runAndWait()
