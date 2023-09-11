import sys
import time

from gtts import gTTS
import tempfile
import pygame


def text_to_speech(text, lang='es'):
    tts = gTTS(text=text, lang=lang)
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    tts.save(temp_file.name)
    return temp_file.name


def reproducir_audio(archivo):
    dispositivo = 'CABLE Input (VB-Audio Virtual Cable)' if len(
        sys.argv) > 1 else 'Auriculares (2- Razer Nari Ultimate - Game)'
    print("Reproduciendo el resultado...")
    pygame.mixer.init(devicename=dispositivo)
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()


def main():
    while True:
        speech_file = text_to_speech(input("Escribe texto: "))
        time.sleep(0)
        reproducir_audio(speech_file)


if __name__ == "__main__":
    main()
