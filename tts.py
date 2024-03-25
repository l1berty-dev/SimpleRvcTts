from .app import tts
import sounddevice as sd
import soundfile as sf
import time


class TTS():
    def __init__(self, model_name, model_root, speed, tts_voice, f0_up_key, f0_method, index_rate, protect):
        self.model_name = model_name
        self.model_root = model_root
        self.speed = speed
        self.tts_voice = tts_voice
        self.f0_up_key = f0_up_key
        self.f0_method = f0_method
        self.index_rate = index_rate
        self.protect = protect

    def get(self, tts_text):
        info, edge_output_filename, result = tts(self.model_name, self.model_root, self.speed, tts_text, self.tts_voice,
                                                 self.f0_up_key, self.f0_method, self.index_rate, self.protect)
        return (result[0], result[1])
    def play(self, data):
        sd.play(data[0], data[1])
        time.sleep(len(data[0]) / data[1])
        sd.stop()

    def save(self, data, filename):
        output_file = filename
        sf.write(output_file, data[0], data[1])