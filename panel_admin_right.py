from tkinter import *
from tkinter import ttk

import tkinter as tk

from functions import click_create_panel, click_create_athlete, click_wallpaper, \
    fullscreen_athlete, create_messages_text
from scroll_text import ScrollText

from styles import style_container, style_entry, style_button, style_entry_frame, invisible_frame, style_frame_label, \
    style_button_special

FON_PANEL = "#4f6369"
FON_FIELD = "#364a4f"
FON_FIELD_MAP = "#cc6b41"
BORDER = "#00f4fc"
TEXT = "white"
ENTRY_BG = "#9dafb0"
ENTRY_TEXT = "#752502"
ENTRY_BG_FOCUSIN = "#b6edf0"
# SELECT_BG = "#946a59"  # выделение текста
BUTTON_BG = "#2a393d"
BUTTON_BORDER = "#ba4216"
BUTTON_BG_PRESSED = "#522a1b"
BUTTON_BG_ACTIVE = "#4f6369"

ENTRY_TEXT_AFTER = "#014145"
SELECT_BG_MARKER = "#946a59" # выделение текста
TEXT_RED = "#ba4216"


class PanelRightTools(tk.Frame):
    """ Структура вкладки 'Инструменты' """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(pady=10, bg=FON_PANEL)

        #################### Прокрутка

        self.canvas = tk.Canvas(self, background=FON_PANEL, highlightthickness=1, highlightbackground=FON_PANEL)
        self.frame = tk.Frame(self.canvas, background=FON_PANEL)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview, style="Custom.Vertical.TScrollbar")
        # self.vsb.set(0.2, 0.3)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.frame.pack(side=TOP, fill=BOTH, expand=True)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas_frame = self.canvas.create_window((0, 0), window=self.frame, anchor="n", tags="self.frame")

        self.frame.bind('<Enter>', self._bound_to_mousewheel)
        self.frame.bind('<Leave>', self._unbound_to_mousewheel)
        self.frame.bind("<Configure>", self.OnFrameConfigure)

        self.canvas.bind('<Configure>', self.FrameWidth)

        ###############################

        self.container_button_athlete = style_container(self.frame)
        self.container_button_athlete.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.label_title_athlete = ttk.Label(self.container_button_athlete, text="Открыть окно (Атлет)",
                                             background=FON_FIELD, foreground=BORDER)
        self.label_title_athlete.pack(side=TOP, pady=5, padx=10, anchor="w", expand=True)

        self.frame_city_year = invisible_frame(self.container_button_athlete)
        self.frame_city_year.pack(side=TOP, fill=BOTH, pady=5, padx=5, anchor="w")

        self.frame_city = style_entry_frame(self.frame_city_year, "Город", pady=5)
        self.frame_city.pack(side=LEFT, pady=5, padx=5, anchor="w")
        self.entry_city = style_entry(self.frame_city, width=29)
        self.entry_city.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_year = style_entry_frame(self.frame_city_year, "Год", pady=5)
        self.frame_year.pack(side=LEFT, pady=5, padx=10, anchor="w")
        self.entry_year = style_entry(self.frame_year)
        self.entry_year.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_button_athlete = invisible_frame(self.container_button_athlete)
        self.frame_button_athlete.pack(side=TOP, fill=BOTH, pady=5, padx=5, anchor="w")

        self.button_create_athlete = style_button_special(self.frame_button_athlete, "Открыть",
                                                          self.button_athlete_window)
        self.button_create_athlete.pack(side=LEFT, pady=5, padx=15, anchor="w", expand=True)

        self.button_fullscreen_athlete = style_button(self.frame_button_athlete, "Режим экрана", fullscreen_athlete)
        self.button_fullscreen_athlete.pack(side=TOP, pady=5, padx=15, anchor="w", expand=True)

        # self.choice_athlete = style_frame_label(self.container_button_athlete, " Вывести на экран ")
        # self.choice_athlete.pack(fill=X, anchor="n", pady=15, padx=20, expand=True)

        # self.button_athlete_sportsmen = style_button(self.choice_athlete, "Спортсмен", click_athlete_sportsmen)
        # self.button_athlete_sportsmen.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)

        # self.button_athlete_table = style_button(self.choice_athlete, "Таблица", click_table)
        # self.button_athlete_table.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)

        # self.button_athlete_wallpaper = style_button(self.choice_athlete, "Реклама", click_wallpaper)
        # self.button_athlete_wallpaper.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)

        ###############################

        self.container_point = style_container(self.frame)
        self.container_point.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.label_title = ttk.Label(self.container_point, text="Создать вкладку управления управления оценками",
                                     background=FON_FIELD, foreground=BORDER)
        self.label_title.pack(side=TOP, pady=5, padx=10, anchor="w", expand=True)

        self.shared_frame = invisible_frame(self.container_point)
        self.shared_frame.pack(side=LEFT, fill=X, pady=15, padx=5, anchor="nw")

        self.frame_title_panel = style_entry_frame(self.shared_frame, "Наименование вкладки", pady=5)
        self.frame_title_panel.pack(side=TOP, pady=5, padx=5, anchor="e")
        self.entry_title_panel = style_entry(self.frame_title_panel, width=15)
        self.entry_title_panel.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_penalty_point = style_entry_frame(self.shared_frame, "Штрафной балл (название)", pady=5)
        self.frame_penalty_point.pack(side=TOP, pady=5, padx=5, anchor="e")
        self.entry_penalty_point = style_entry(self.frame_penalty_point)
        self.entry_penalty_point.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_total = style_entry_frame(self.shared_frame, "Общая оценка (название)", pady=5)
        self.frame_total.pack(side=TOP, pady=5, padx=5, anchor="e")
        self.entry_total = style_entry(self.frame_total)
        self.entry_total.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_point_all = style_frame_label(self.container_point, " Н а з в а н и я  о ц е н о к ")
        self.frame_point_all.pack(side=TOP, fill=X, pady=15, padx=10, anchor="ne", expand=True)

        self.frame_point_top = invisible_frame(self.frame_point_all)
        self.frame_point_top.pack(side=TOP, fill=X, pady=0, padx=0, anchor="n", expand=True)

        self.frame_1 = invisible_frame(self.frame_point_top)
        self.frame_1.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)
        self.entry_1 = style_entry(self.frame_1)
        self.entry_1.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_2 = invisible_frame(self.frame_point_top)
        self.frame_2.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)
        self.entry_2 = style_entry(self.frame_2)
        self.entry_2.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_3 = invisible_frame(self.frame_point_top)
        self.frame_3.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)
        self.entry_3 = style_entry(self.frame_3)
        self.entry_3.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_point_bottom = invisible_frame(self.frame_point_all)
        self.frame_point_bottom.pack(side=TOP, fill=X, pady=0, padx=0, anchor="n", expand=True)

        self.frame_4 = invisible_frame(self.frame_point_bottom)
        self.frame_4.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)
        self.entry_4 = style_entry(self.frame_4)
        self.entry_4.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_5 = invisible_frame(self.frame_point_bottom)
        self.frame_5.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)
        self.entry_5 = style_entry(self.frame_5)
        self.entry_5.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame_6 = invisible_frame(self.frame_point_bottom)
        self.frame_6.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)
        self.entry_6 = style_entry(self.frame_6)
        self.entry_6.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.button = style_button_special(self.container_point, "Создать", self.button_create_panel)
        self.button.pack(side=TOP, pady=10, padx=10, anchor="n", expand=True)

        ###############################



        ###############################

        self.container_button_scoreboard = style_container(self.frame)
        self.container_button_scoreboard.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.label_title_scoreboard = ttk.Label(self.container_button_scoreboard, text="Запустить слайды",
                                                background=FON_FIELD, foreground=BORDER)
        self.label_title_scoreboard.pack(side=TOP, pady=5, padx=10, anchor="w", expand=True)

        self.frame_button_scoreboard = invisible_frame(self.container_button_scoreboard)
        self.frame_button_scoreboard.pack(side=LEFT, fill=BOTH, pady=5, padx=5, anchor="c")

        # self.button_create_scoreboard = style_button_special(self.frame_button_scoreboard,
        #                                                      "Создать", click_create_scoreboard)
        # self.button_create_scoreboard.pack(side=LEFT, pady=5, padx=15, anchor="c", expand=True)

        self.choice_scoreboard = style_frame_label(self.container_button_scoreboard, " Вывести на экран ")
        self.choice_scoreboard.pack(fill=X, anchor="n", pady=15, padx=20, expand=True)

        # self.button_scoreboard_sportsmen = style_button(self.choice_scoreboard, "Спортсмен", click_sportsmen)
        # self.button_scoreboard_sportsmen.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)

        # self.button_scoreboard_table = style_button(self.choice_scoreboard, "Таблица", click_table)
        # self.button_scoreboard_table.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)

        self.button_scoreboard_wallpaper = style_button(self.choice_scoreboard, "На экран", click_wallpaper)
        self.button_scoreboard_wallpaper.pack(side=LEFT, pady=5, padx=5, anchor=CENTER, expand=True)

        ##################### Сообщения

        self.container_messages = style_container(self.frame)
        self.container_messages.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.label_title_messages = ttk.Label(self.container_messages, text="Р е е с т р  с о б ы т и й",
                                              background=FON_FIELD, foreground=BORDER)
        self.label_title_messages.pack(side=TOP, pady=5, padx=10, anchor="n", expand=True)

        self.messages = ScrollText(self.container_messages)
        self.messages.text.insert(tk.END, "__________________________\n\n ")
        self.messages.pack()

    def _bound_to_mousewheel(self, event):
        """ Привязывает к колесу мыши виджет с указателем мыши. """

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        """ Отвзяывает от колеса мыши виджет без указателя мыши. """

        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """ Прокручивает холст по колесу мыши. """

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def OnFrameConfigure(self, event):
        """ Задает область прокрутки. """

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def FrameWidth(self, event):
        """ Растягивает виджеты по холсту. (?) """

        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def button_create_panel(self):
        """ Создает вкладку на левой панели. """

        click_create_panel(self.entry_title_panel.get(),
                           self.entry_1.get(),
                           self.entry_2.get(),
                           self.entry_3.get(),
                           self.entry_4.get(),
                           self.entry_5.get(),
                           self.entry_6.get(),
                           self.entry_penalty_point.get(),
                           self.entry_total.get(),
                           )

    def button_athlete_window(self):
        """ Создает окно Атлет. """

        click_create_athlete(self.entry_city.get(), self.entry_year.get())

    def messages_text(self, text, color):
        """ Создает уведомление. """

        if color:
            self.messages.text.insert("3.0", text)
        else:
            self.messages.text.insert("3.0", text, 'tag_red_text')



    # def blink_button(self):
    #     """  """
    #
    #     change_color_button_red(self.button_create_athlete)
    #     self.frame_button_athlete.after(120, change_color_button_gray, self.button_create_athlete)
    #     self.frame_button_athlete.after(240, change_color_button_red, self.button_create_athlete)
    #     self.frame_button_athlete.after(360, change_color_button_gray, self.button_create_athlete)
    #     self.frame_button_athlete.after(480, change_color_button_red, self.button_create_athlete)
    #
    #     self.button_create_athlete = style_button_special(self.frame_button_athlete, "Открыть",
    #                                                       self.button_athlete_window)


class PanelRightSettings(tk.Frame):
    """ Структура вкладки 'Настройки'. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.style_field = None
        self.frame = None
        self.label = None
        self.entry_frame = None
        self.entry = None

        self.configure(pady=35, bg=FON_PANEL)
