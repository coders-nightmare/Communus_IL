# Communus_IL
It is Text To Speech , Speech To Text , Image To Text,Speech single python program.

Steps To Make It Work In your System:

1)clone the repository
2)From installation folder install tesseract-ocr with default settings
3)Re-check it's Location 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# 4)This Step is little bit tricky:-
   - 1st run python in cmd (if not, 1st install and add it to path and then run)
   - now check python version (Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32)
   - download specific pyAudio version from (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
   - in my case i have linked 3.8 AMD64 (for reference https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14 
     go here)
   - now run pip install file-location 
   - example :- (pip install "D:\Study\PYTHON\Text to speech\installations\PyAudio-0.2.11-cp38-cp38-win_amd64.whl")
5) now run:-  pip install -r requirements.txt
6) Finally You can run program in your machine

(Note : I have attached win32 and AMD64 3.8 version for pyaudio)
