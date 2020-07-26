import pytesseract
from PIL import Image
import speech_recognition as s_r
from googletrans import Translator
from gtts import gTTS
import os


def mtts(result):
    language = input("language")
    translator = Translator()
    k = translator.translate(result, dest=language)
    myobj = gTTS(text=k.text, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")


n = True
while(n == True):
    try:
        option = int(input(
            "1-speech to text\n2-text to speech\n3-image to speech\nPress any key for exit"))
        if(option == 2):
            mytext = input("enter text")
            mtts(mytext)
        elif(option == 3):
            h = input("image with extention")
            img = Image.open('rit.png')
            print(img)
            pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
            result = pytesseract.image_to_string(img)
            with open('mytext.txt', mode='w') as file:
                file.write(result)
                print(result)
            mtts(result)
        elif(option == 1):
            print(s_r.__version__)
            r = s_r.Recognizer()
            my_mic = s_r.Microphone(device_index=1)
            with my_mic as source:
                print("Say now!!!!")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                k = r.recognize_google(audio)
                print(k)
                mtts(k)
            except:
                print("not received")
        else:
            n = False
    except:
        print("ERROR")
        exit()
