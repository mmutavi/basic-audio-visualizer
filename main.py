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

NUM_BARS = 32


class AudioVisualizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Live Audio Visualizer")
        self.geometry("700x480")
        self.configure(fg_color=BG)

        top = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=12)
        top.pack(fill="x", padx=20, pady=20)
        self.toggle_btn = ctk.CTkButton(top, text="Start Listening", fg_color="#2a2a30",
                                         command=self._toggle)
        self.toggle_btn.pack(side="left", padx=16, pady=14)
        self.status_var = ctk.StringVar(value="Idle")
        ctk.CTkLabel(top, textvariable=self.status_var, text_color="#8a8a8a").pack(side="left", padx=10)

        self.canvas = ctk.CTkCanvas(self, bg=PANEL, height=320, width=660, highlightthickness=0)
        self.canvas.pack(padx=20, pady=(0, 20))