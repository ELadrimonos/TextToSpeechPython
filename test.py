import time
from pygame import mixer, _sdl2 as devicer

mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Initialize it with the correct device
print("Inputs:", devicer.audio.get_audio_device_names(True))
print("Outputs:", devicer.audio.get_audio_device_names(False))
mixer.music.play() # Play it

while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)