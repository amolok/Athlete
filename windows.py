import time
from tkinter import *
from tkinter import ttk

import tkinter as tk

from sportsmen import Sportsmen
from styles import style_notebook
from wallpaper import Wallpaper
import functions

TEST = "#fa552f"

FON = "#687375"
FON_PANEL = "#364a4f"
TAB = "#687375"
TAB_MAP = "#4f6369"
BORDER = "#00f4fc"
TEXT = "white"
TEXT_2 = "#00f4fc"
TEXT_CITY = "#00f4fc"


class Admin(Tk):
    """ Окно 'Административная панель'. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Административная панель")
        self.image_icon_small = tk.PhotoImage(file='logo_24.png')
        self.image_icon = tk.PhotoImage(file='logo_32.png')
        self.iconphoto(True, self.image_icon, self.image_icon_small)
        # self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight())) # Сделать полный экран ?
        self.geometry("1350x750+10+10")
        self.configure(bg=FON)
        # self.style_admin = style_notebook(self)  # убрать ?

class Athlete(Toplevel):
    """ Окно Атлет. """

    def __init__(self, *args):
        super().__init__()

        self.title("Атлет")
        self.geometry("1150x550+700+550")
        self.configure(bg=FON)

        self.wallpaper = None
        self.athlete_sportsmen = None
        self.state = False # полный экран / окно
        self.text = ' '.join(" " + str(args[0]) + " " + str(args[1]) + " ").upper()

        self.frame_label = tk.LabelFrame(self, labelanchor="nw", text=self.text,
                                         font="Arial 22 bold", bg=FON_PANEL, fg=TEXT_CITY, borderwidth=1,
                                         relief=RAISED, padx=10, pady=25)
        self.frame_label.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)

    def create_sportsmen(self):
        """ Удаляет данные предыдущего спортсмена, если существует.
        Останавливает показ слайдов, если он запущен.
        Создает экран 'Спортсмен' с результатами. """

        if self.athlete_sportsmen:
            # self.slide_position_end()
            self.athlete_sportsmen.destroy()
            self.athlete_sportsmen = Sportsmen(self, self.text)

        elif self.wallpaper:
            self.wallpaper.status_wallpaper = False
            self.wallpaper.destroy()
            self.athlete_sportsmen = Sportsmen(self, self.text)
        else:
            self.athlete_sportsmen = Sportsmen(self, self.text)

    def create_scoreboard(self):
        """ Создает экран 'Табло' с турнирной таблицей. """

        pass

        # создать класс Scoreboard()
        # self.athlete_sportsmen = Scoreboard(self.frame_label)

    def switch_wallpaper(self):
        """ Создает экран 'Показ слайдов'. """

        image_files = [
            'logo_white_1024.png',
            'vertical.png',
            'feder.png',
        ]

        self.wallpaper = Wallpaper(self, image_files, True)
        # self.scoreboard_wallpaper = Wallpaper(self, image_files)

        # self.scoreboard_wallpaper.pack()

    def close_athlete(self):
        """ Останавливает потоки, закрывает окно. """

        if self.wallpaper:
            self.wallpaper.status_wallpaper = False
        self.destroy()
        functions.athlete_window = None
        functions.create_messages_text(f"Окно Атлет закрыто")

    # def slide_position_end(self):
    #     """ Перемещает на экране спортсмена и его результаты с центра направо.
    #      Вызывает функцию удаления спортсмена. """
    #
    #     pos = self.athlete_sportsmen.frame_sportsman.place_info()
    #     print(f"позиция на экране {float(pos['relx'])}")
    #
    #     x = float(pos['relx'])
    #     if x < 1.5:
    #         # self.frame_cup.place(relx=x + 0.05)
    #         # self.frame_category.place(relx=x + 0.05)
    #         self.athlete_sportsmen.frame_sportsman.place(relx=x + 0.05)
    #         # self.frame_total.place(relx=x + 0.05)
    #         # self.frame_position.place(relx=x + 0.05)
    #         # self.frame_points.place(relx=x + 0.05)
    #         self.after(10, self.slide_position_end)
    #     else:
    #         self.destroy_sportsmen()
    #
    #
    #
    # def destroy_sportsmen(self):
    #     """ Удаляет спортсмена. """
    #
    #     self.athlete_sportsmen.destroy()


    # self.athlete_sportsmen.frame_cup.destroy()
    # self.athlete_sportsmen.frame_category.destroy()
    # self.athlete_sportsmen.frame_sportsman.destroy()
    # self.athlete_sportsmen.frame_total.destroy()
    # self.athlete_sportsmen.frame_position.destroy()
    # self.athlete_sportsmen.frame_points.destroy()

# class Scoreboard(Toplevel):
#     """ Окно 2 (Табло). """
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.scoreboard_wallpaper = None
#         self.title("Окно 2 (Табло)")
#         self.geometry("1350x750+510+310")
#         self.configure(bg=FON)
#
#
#
#     def switch_sportsmen(self):
#         """ Вызывает функцию создания спортсмена ----- ПЕРЕДЕЛАТЬ - это переключение на экран спортсмена, а не создание. """
#
#         self.scoreboard_sportsmen = Sportsmen(self)
