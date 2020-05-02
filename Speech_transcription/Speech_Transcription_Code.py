from googletrans import Translator
import pyaudio                                
import speech_recognition as sr
import unicodedata
import os
translator=Translator()
r = sr.Recognizer()
print ("Please say your phrase")
with sr.Microphone() as source:
	print('speak')                
	audio = r.listen(source)                 
try:
	print("You said: " + r.recognize_google(audio,language='ta-IN'))    
	microphone_input  = r.recognize_google(audio,language='ta-IN')     
except LookupError:                           
	print("Could not understand audio")
    

phrase = translator.translate(microphone_input,src='ta')
#print(phrase) 

read = str(phrase)   
sentence = read.find('text') 
end_of_phrase = read.find(' pronunciation') 
final_phrase = read[sentence+5 : end_of_phrase] 
print(final_phrase) 
#if final_phrase == 'what is the time,':
#	os.system('espeak \'8:15\'')