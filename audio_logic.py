"""
Microphone capture and FFT banding. Uses sounddevice for the input stream
(reads happen synchronously via a small ring buffer) and numpy for the FFT
and log-spaced frequency banding.
"""