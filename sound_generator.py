import pyaudio
import numpy as np
from sample_generator import get_sine_samples


class SoundGenerator:

    def __init__(self):
        # set default parameters
        self.stream = None
        self.samples = None
        self.volume = 0.5  # range [0.0, 1.0]
        self.fs = 44100  # sampling rate, Hz, must be integer
        self.duration = 1.0  # in seconds, may be float
        self.channels = 1
        self._p = pyaudio.PyAudio()
        self._is_playing = False

    def start_play(self):
        if not self._is_playing:
            self.stream = self._p.open(format=pyaudio.paFloat32,
                                       channels=self.channels,
                                       rate=self.fs,
                                       output=True)
            self._is_playing = True
            # play. May repeat with different volume values (if done interactively)
            self.stream.write(self.samples)
            self.stop_play()

    def stop_play(self):
        if self._is_playing:
            self.stream.stop_stream()
            self.stream.close()
            self._is_playing = False

    def beep_sound(self):
        f = 440.0  # sine frequency, Hz, may be float

        # generate samples, note conversion to float32 array
        samples = get_sine_samples(duration=self.duration, sampling_rate=self.fs, frequency=f)
        self.generate_using_samples(samples=samples)

    def generate_using_samples(self, samples):
        self.samples = samples

    def __del__(self):
        self._p.terminate()

if __name__ == '__main__':
    SoundGenerator().beep_sound()
