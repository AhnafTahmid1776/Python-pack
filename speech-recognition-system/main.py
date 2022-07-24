import googletrans
import speech_recognition as sr
listener = sr.Recognizer()
translator= googletrans.Translator()


try:
    with sr. Microphone() as source:
       print('listening....')
       listener.adjust_for_ambient_noise(source)
       voice = listener.listen(source)
       command = listener.recognize_google(voice)
       listener.recognize_google(voice)
       print(command)
except :
       pass
