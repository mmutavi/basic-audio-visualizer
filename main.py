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

        self.stream = None
        self.running = False
        self._draw_bars([0.0] * NUM_BARS)

    def _toggle(self):
        if self.running:
            self.running = False
            self.toggle_btn.configure(text="Start Listening")
            self.status_var.set("Idle")
            logic.stop_stream(self.stream)
            self.stream = None
        else:
            try:
                self.stream = logic.start_stream()
            except Exception as e:
                self.status_var.set(f"Mic error: {e}")
                return
            self.running = True
            self.toggle_btn.configure(text="Stop Listening")
            self.status_var.set("Listening...")
            self._update_loop()

    def _update_loop(self):
        if not self.running:
            return
        levels = logic.get_bar_levels(self.stream, NUM_BARS)
        self._draw_bars(levels)
        self.after(30, self._update_loop)

    def _draw_bars(self, levels):
        self.canvas.delete("all")
        width = 660
        height = 320
        gap = 4
        bar_width = (width - gap * (NUM_BARS + 1)) / NUM_BARS