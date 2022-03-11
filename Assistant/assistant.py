"""
third-party imports
"""

# importing speech recognition package from google api
import os # to save/open files
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech

class Assistant:
    """
    This class contains all the methods that enable the assistant's
    speaking and listening capabilities.
    """
    def __init__(self):
        # pylint: disable = E0602
        # limit 5 secs
        self.time_out = 5
        # initialization of the rest of the parameters
        self.output = ""
        self.to_speak = ""
        self.input = ""
        self.r_object = sr.Recognizer()
        self.intro = '''Hola, mi nombre es Cortana. Soy tu asistente para la búsqueda
                de vulnerabilidades de ciberseguridad.'''
        self.creador = "He sido desarrollada por Luis Muñiz García."
        self.file = "last_audio_record.mp3"
        # pylint: disable = R0902

    def speaks(self,output):
        """
        args: output
        returns: audio output
        """
        self.output = output
        print("Usuario : ", output)
        self.to_speak = gTTS(text = output, lang ='es', slow = False)
        # saving the audio file given by google text to speech
        self.to_speak.save(self.file)
        # playsound package is used to play the same file.
        playsound.playsound(self.file, True)
        # remove the listened audio file.
        os.remove(self.file)

    def listen(self):
        """
        returns: text if success, 0 otherwise
        """
        with sr.Microphone() as source:
            print("Habla...")
            # recording the audio using speech recognition
            audio = self.r_object.listen(source, phrase_time_limit = self.time_out)
        print("Para.")

        try:
            text = self.r_object.recognize_google(audio, language ='es-ES')
            print("Tú : ", text)
            return text
        except Exception as exception:
            self.speaks("No te he entendido. Por favor, inténtalo otra vez.")
            print(exception)
            return 0
    def process_text(self,input):
        """
        args: input
        returns: nothing
        """
        self.input = input
        try:
            if 'busca' in self.input or 'pon' in self.input:
                print("WIP")
                #return
            elif "quien eres" in self.input:
                self.speaks(self.intro)
                #return
            elif "quien es tu creador" in self.input or "creador" in self.input:
                self.speaks(self.creador)
                #return
            else:
                self.speaks("Puedo buscarlo en la web por ti. ¿Quieres?")
                ans = self.listen()
                if 'si' in str(ans) or 'vale' in str(ans):
                    print("WIP")
                else:
                    return
        except Exception as exception:
            print(exception)
            self.speaks("No te he entendido, puedo buscarlo en la web por ti. ¿Quieres?")
            ans = self.listen()
            if 'si' in str(ans) or 'vale' in str(ans):
                #search_web(input)
                print("WIP")

# Driver Code
if __name__ == "__main__":
    assistant = Assistant()
    assistant.speaks("¡Hola! Mi nombre es Cortana. ¿En qué puedo ayudarte?")
    name = assistant.listen()
    assistant.speaks("Hola, "+name+'.')
    while 1:
        assistant.speaks("¿Qué necesitas?")
        text = assistant.listen().lower()

        if text == 0:
            continue

        if "salir" in str(text) or "eso es todo" in str(text) or "duerme" in str(text):
            assistant.speaks("Pasando a modo ahorro de energía.")
            break

        # calling process text to process the query
        assistant.process_text(text)
