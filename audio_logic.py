"""
Microphone capture and FFT banding. Uses sounddevice for the input stream
(reads happen synchronously via a small ring buffer) and numpy for the FFT
and log-spaced frequency banding.
"""

import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100
BLOCK_SIZE = 1024


class _Stream:
    def __init__(self):
        self.buffer = np.zeros(BLOCK_SIZE, dtype=np.float32)
        self.stream = sd.InputStream(
            channels=1, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE,
            callback=self._callback,
        )
        self.stream.start()

    def _callback(self, indata, frames, time_info, status):
        self.buffer = indata[:, 0].copy()

    def close(self):
        self.stream.stop()
        self.stream.close()


def start_stream():
    return _Stream()


def stop_stream(stream):
    if stream is not None:
        stream.close()


def get_bar_levels(stream, num_bars):
    samples = stream.buffer
    windowed = samples * np.hanning(len(samples))
    spectrum = np.abs(np.fft.rfft(windowed))