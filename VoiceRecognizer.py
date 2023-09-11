import sys

import speech_recognition as sr
from gtts import gTTS
import tempfile
import pygame

from main import text_to_speech, reproducir_audio


def reconocer_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        print("Convirtiendo audio a texto...")
        text = recognizer.recognize_google(audio, language='es')
        print("Texto detectado:", text)

        print("Convirtiendo texto a voz...")
        speech_file = text_to_speech(text)
        reproducir_audio(speech_file)

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError:
        print("No se pudo conectar con el servicio de reconocimiento de voz.")


def main():
    while 1:
        print("Habla algo...")
        reconocer_voz()


if __name__ == "__main__":
    main()
