"""
Live Audio Visualizer

Listens to your default microphone and draws a real-time frequency bar
visualizer on a plain canvas. All the audio math (FFT, banding, smoothing)
lives in audio_logic.py so this file only deals with drawing.
"""