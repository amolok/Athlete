from tkinter import *
from tkinter import ttk

import tkinter as tk

from panel_admin_left import PanelLeft
from panel_admin_right import PanelRightTools, PanelRightSettings
from styles import style_notebook

# from functions import sportsman
# from styles import style_button, style_entry, style_container, style_frame, style_frame_label, frame_label_element

FON_PANEL = "#4f6369"
FON_FIELD = "#364a4f"
FON_FIELD_MAP = "#cc6b41"
BORDER = "#00f4fc"
TEXT = "white"
ENTRY_BG = "#9dafb0"
ENTRY_TEXT = "#752502"
ENTRY_BG_FOCUSIN = "#c5d8d9"
SELECT_BG_MARKER = "#946a59"  # выделение текста

FON_WALLPAPER = "#06101c"


class AdminLeft(ttk.Notebook):
    """ Блокнот в левой админке. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.notebook_frame = None
        self.style_admin = style_notebook(self)
        self.panel_left_logo()

    def panel_left_logo(self):
        """ Вкладка 'Главная' (логотип). """

        global athlete_logo

        # left_logo = ttk.Label(self, text="Электронно-судейская платформа А Т Л Е Т", background=FON_FIELD, foreground=TEXT)
        # left_logo.pack(side=TOP, fill=BOTH, anchor="w", expand=True)

        container_image = tk.Frame(self, background=FON_FIELD, borderwidth=0)
        # container_image.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)
        container_image.pack(side=TOP, fill=BOTH, expand=True)


        # pady = 35, padx = 50,
        athlete_logo = tk.PhotoImage(file='logo_green_614.png', master=container_image)

        logo = tk.Label(container_image, image=athlete_logo, anchor=CENTER, relief=FLAT, bd=0)
        logo.pack(expand=True)

        self.add(container_image, text="Главная")

    def panel_left(self, text, point_1, point_2, point_3, point_4, point_5, point_6, point_penalty, total):
        """ Вкладка в блокноте. """

        self.notebook_frame = PanelLeft(point_1, point_2, point_3, point_4, point_5, point_6, point_penalty, total)
        self.notebook_frame.pack(fill=BOTH, expand=True)
        self.add(self.notebook_frame, text=text)
        self.select(self.notebook_frame)


class AdminRight(ttk.Notebook):
    """ Блокнот в правой админке. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.notebook_frame = None
        self.style_admin = style_notebook(self)
        self.right_tools = self.panel_right_tools()
        self.panel_right_settings()


    def panel_right_tools(self):
        """ Создает вкладку 'Инструменты'. """

        self.notebook_frame = PanelRightTools()
        self.notebook_frame.pack(fill=BOTH, expand=True)
        self.add(self.notebook_frame, text="Инструменты")

        return self.notebook_frame

    def panel_right_settings(self):
        """ Создает вкладку 'Настройки'. """

        self.notebook_frame = PanelRightSettings()
        self.notebook_frame.pack(fill=BOTH, expand=True)
        self.add(self.notebook_frame, text="Настройки")
