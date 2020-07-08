from googletrans import Translator
from gtts import gTTS
import os
mytext = input("enter text")
language = input("language")
translator = Translator()
k=translator.translate(mytext, dest=language)
myobj = gTTS(text=k.text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")

