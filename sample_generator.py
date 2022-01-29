import numpy as np


def get_sine_samples(duration, sampling_rate, frequency):
    f = 440.0  # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(sampling_rate * duration) * f / sampling_rate)).astype(
        np.float32).tobytes()

    return samples


if __name__ == '__main__':
    get_sine_samples()
