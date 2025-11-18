from tkinter import *
from tkinter import ttk
import tkinter as tk

from itertools import cycle


FON_WALLPAPER = "white"


class Wallpaper(tk.Frame):
    """ Экран показа слайдов. """

    def __init__(self, parent, image_files, status=False):
        super().__init__()

        self.status_wallpaper = status

        self.container_image = tk.Frame(parent, background=FON_WALLPAPER, borderwidth=0)
        self.container_image.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)

        self.delay = 10000
        self.delay_start = self.delay + 2000

        global pictures
        self.pictures = cycle(tk.PhotoImage(file=image)
                              for image in image_files)
        self.picture_display = tk.Label(parent, anchor=CENTER, background=FON_WALLPAPER, relief=FLAT, bd=0)
        self.picture_display.place(relx=-0.3, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)

        self.show_slides()

    def show_slides(self):
        """ Чередует логотипы по кругу. """

        if self.status_wallpaper:
            img_object = next(self.pictures)
            self.picture_display.config(image=img_object)
            self.picture_display.place(relx=-0.3)
            self.slide_position()
            self.after(self.delay_start, self.show_slides)
        else:
            print(f"Прокрутка слайдов остановлена")

    def slide_position(self):
        """ Перемещает слайд слева-направо. """

        if self.status_wallpaper:
            pos = self.picture_display.place_info()
            x = float(pos['relx'])
            if x < 0.5:
                self.picture_display.place(relx=x + 0.05)
                self.after(10, self.slide_position)
            elif x == 0.5:
                self.picture_display.place(relx=x + 0.0001)
                self.after(self.delay, self.slide_position)
            elif x < 1.3:
                self.picture_display.place(relx=x + 0.05)
                self.after(10, self.slide_position)
            else:
                pass
        else:
            print(f"Перемещение слайда остановлено")

    # def stop_show_slides(self):
    #     """ Остановка показа слайдов. """
    #
    #     pass
