# Live Audio Visualizer

A real-time frequency bar visualizer for your microphone. Sound comes in
through `sounddevice`, gets FFT'd and split into log-spaced frequency bands
in `audio_logic.py`, and gets drawn as bars on a plain canvas.

## Setup

    pip install -r requirements.txt
    python main.py

If you get a "no default input device" error, check your system sound
settings to make sure a microphone is set as the default input.
