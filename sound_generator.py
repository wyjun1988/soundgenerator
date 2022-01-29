import pyaudio
import numpy as np
from sample_generator import get_sine_samples


class SoundGenerator:

    def __init__(self):
        # set default parameters
        self.volume = 0.5  # range [0.0, 1.0]
        self.fs = 44100  # sampling rate, Hz, must be integer
        self.duration = 1.0  # in seconds, may be float
        self.channels = 1
        self._p = pyaudio.PyAudio()
        self._is_playing = False

    def _start_play(self):
        stream = self._p.open(format=pyaudio.paFloat32,
                              channels=self.channels,
                              rate=self.fs,
                              output=True)
        self.is_playing = True
        return stream

    def _stop_play(self):
        self._p.terminate()
        self.is_playing = False

    def beep_sound(self):
        f = 440.0  # sine frequency, Hz, may be float

        # generate samples, note conversion to float32 array
        samples = get_sine_samples(duration=self.duration, sampling_rate=self.fs, frequency=f)
        self.generate_using_samples(samples=samples)

    def generate_using_samples(self, samples):
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = self._start_play()
        # play. May repeat with different volume values (if done interactively)
        stream.write(samples)
        stream.stop_stream()
        stream.close()
        self._stop_play()


if __name__ == '__main__':
    SoundGenerator().beep_sound()
