from tkinter import *
from tkinter import ttk
import tkinter as tk

from styles import style_scrolled_text

SCROLL_TEXT_BG = "#e66b3e"
TEXT = "white"
SELECT_BG_MARKER = "#946a59"
TEXT_RED = "#a3020c"


class ScrollText(ttk.Frame):

    def __init__(self, parent):
        super().__init__()

        style_scrolled_text()

        self.vscrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, style="Custom.Vertical.TScrollbar")
        self.text = tk.Text(parent, font=("Arial", 9, "bold"), yscrollcommand=self.vscrollbar.set, wrap="word",
                            background=SCROLL_TEXT_BG, foreground=TEXT, height=12, highlightbackground=TEXT,
                            selectbackground=SELECT_BG_MARKER, highlightcolor=TEXT,)

        self.vscrollbar.config(command=self.text.yview)
        self.text.tag_config('tag_red_text', foreground=TEXT_RED)

        # self.vscrollbar.pack(side=RIGHT, fill=Y, pady=5, padx=0)
        self.text.pack(side=TOP, fill=X, pady=15, padx=15, anchor="n", expand=True)

