import sys

import speech_recognition as sr
from gtts import gTTS
import tempfile
import pygame

from main import text_to_speech


def main():
    recognizer = sr.Recognizer()
    dispositivo = 'CABLE Input (VB-Audio Virtual Cable)' if len(sys.argv) > 1 else 'Auriculares (2- Razer Nari Ultimate - Game)'
    while (1):
        print("Habla algo...")

        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        try:
            print("Convirtiendo audio a texto...")
            text = recognizer.recognize_google(audio, language='es')
            print("Texto detectado:", text)

            print("Convirtiendo texto a voz...")
            speech_file = text_to_speech(text)

            print("Reproduciendo el resultado...")

            pygame.mixer.init(devicename = dispositivo)
            pygame.mixer.music.load(speech_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pass

            pygame.mixer.quit()

        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError:
            print("No se pudo conectar con el servicio de reconocimiento de voz.")


if __name__ == "__main__":
    main()
