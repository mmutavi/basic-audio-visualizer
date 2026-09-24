"""
Live Audio Visualizer

Listens to your default microphone and draws a real-time frequency bar
visualizer on a plain canvas. All the audio math (FFT, banding, smoothing)
lives in audio_logic.py so this file only deals with drawing.
"""

import customtkinter as ctk

import audio_logic as logic

ctk.set_appearance_mode("dark")

BG = "#0a0a0d"
PANEL = "#161619"
ACCENT = "#8b5cf6"