from tkinter import *
from tkinter import ttk
import tkinter as tk

# from functions import slide_position_start

FON_PANEL = "#364a4f"
FON_FRAME = "#4f6369"
TEXT_CITY = "#00f4fc"
TEXT_CUP = "white"


class Scoreboard(tk.Frame):
    """ Экран 'Таблица с результатами'. """

    status_publication = False

    def __init__(self, parent, text):
        super().__init__()

        self.text = text

        # self.frame_label = tk.LabelFrame(parent, labelanchor="nw", text=self.text,
        #                                  font="Arial 22 bold", bg=FON_PANEL, fg=TEXT_CITY, borderwidth=1,
        #                                  relief=RAISED, padx=10, pady=25)
        # self.frame_label.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)

        self.frame_label = parent.frame_label

        self.frame_cup = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        self.frame_cup.place(relx=-0.5, rely=0.08, relwidth=0.75, anchor=CENTER)

        self.frame_category = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        self.frame_category.place(relx=1.5, rely=0.20, relwidth=0.75, anchor=CENTER)

        # self.frame_sportsman = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        # self.frame_sportsman.place(relx=-0.5, rely=0.40, relwidth=0.75, anchor=CENTER)
        #
        # self.frame_total = tk.Frame(self.frame_label, bg=FON_FRAME, borderwidth=0, relief=RIDGE)
        # self.frame_total.place(relx=-0.5, rely=0.50, relwidth=0.75, anchor=CENTER)
        #
        # self.frame_position = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        # self.frame_position.place(relx=1.5, rely=0.50, relwidth=0.75, anchor=CENTER)
        #
        # self.frame_points = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        # self.frame_points.place(relx=-0.5, rely=0.8, relwidth=0.80, anchor=CENTER)


        # self.frame_cup = None
        self.label_cup = None
        self.label_category = None
        self.label_sportsman = None
        self.label_total = None
        self.label_position = None
        self.label_points = None

    def result_sportsmen(self, cup, category, sportsman, entry_1, entry_2, entry_3, entry_7,
                         entry_total, sportsmen_position):
        """ Выводит результаты спортсмена. """

        # self.slide_position_end()
        self.frame_cup.destroy()
        self.frame_category.destroy()
        self.frame_sportsman.destroy()
        self.frame_total.destroy()
        self.frame_position.destroy()

        self.frame_cup = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        self.frame_cup.place(relx=-0.5, rely=0.08, relwidth=0.75, anchor=CENTER)
        self.label_cup = ttk.Label(self.frame_cup, font=("Arial", 38, "bold"),
                                   foreground=TEXT_CUP, background=FON_PANEL)
        self.label_cup.pack(anchor="center", expand=True)
        self.label_cup["text"] = cup
        self.after(100, self.slide_position_cup())

        self.frame_category = tk.Frame(self.frame_label, bg=FON_PANEL, borderwidth=0, relief=RIDGE)
        self.frame_category.place(relx=1.5, rely=0.20, relwidth=0.75, anchor=CENTER)
        self.label_category = ttk.Label(self.frame_category, font=("Arial", 24, "bold"),
                                        foreground=TEXT_CUP, background=FON_PANEL)
        self.label_category.pack(anchor="center", expand=True)
        self.label_category["text"] = category

        self.frame_sportsman = tk.Frame(self.frame_label, bg=FON_FRAME, borderwidth=0, relief=RIDGE)
        self.frame_sportsman.place(relx=-0.5, rely=0.4, relwidth=0.75, anchor=CENTER)
        self.label_sportsman = ttk.Label(self.frame_sportsman, font=("Arial", 68, "bold"),
                                         foreground=TEXT_CUP, background=FON_FRAME)
        self.label_sportsman.pack(anchor="center", expand=True)
        self.label_sportsman["text"] = sportsman.upper()

        self.frame_total = tk.Frame(self.frame_label, bg=FON_FRAME, borderwidth=0, relief=RIDGE)
        self.frame_total.place(relx=-0.5, rely=0.6, relwidth=0.20, anchor=CENTER)
        self.label_total = ttk.Label(self.frame_total, font=("Arial", 68, "bold"),
                                     foreground=TEXT_CUP, background=FON_FRAME)
        self.label_total.pack(anchor="center", expand=True)
        self.label_total["text"] = entry_total

        self.frame_position = tk.Frame(self.frame_label, bg=FON_FRAME, borderwidth=0, relief=RIDGE)
        self.frame_position.place(relx=1.5, rely=0.6, relwidth=0.20, anchor=CENTER)
        self.label_position = ttk.Label(self.frame_position, font=("Arial", 68, "bold"),
                                        foreground=TEXT_CUP, background=FON_FRAME)
        self.label_position.pack(anchor="center", expand=True)
        self.label_position["text"] = sportsmen_position

        self.frame_points = tk.Frame(self.frame_label, bg=FON_FRAME, borderwidth=0, relief=RIDGE)
        self.frame_points.place(relx=-0.5, rely=0.8, relwidth=0.80, anchor=CENTER)
        self.label_points = ttk.Label(self.frame_points, font=("Arial", 48, "bold"),
                                      foreground=TEXT_CUP, background=FON_FRAME)
        self.label_points.pack(anchor="center", expand=True)
        self.label_points["text"] = entry_1 + entry_2 + entry_3 + entry_7


        # self.point_1["text"] = entry_1
        # self.point_2["text"] = entry_2
        # self.point_3["text"] = entry_3
        # self.point_7["text"] = entry_7


    def slide_position_cup(self):
        """ Перемещает название турнира слева до центра. """

        pos = self.frame_cup.place_info()
        x = float(pos['relx'])
        if x < 0.5:
            self.frame_cup.place(relx=x + 0.05)
            self.after(10, self.slide_position_cup)
        else:
            self.after(200, self.slide_position_category())

    def slide_position_category(self):
        """ Перемещает наименование категории справа до центра. """

        pos = self.frame_category.place_info()
        x = float(pos['relx'])
        if x > 0.5:
            self.frame_category.place(relx=x - 0.05)
            self.after(10, self.slide_position_category)
        else:
            self.after(200, self.slide_position_sportsman())

    def slide_position_sportsman(self):
        """ Перемещает имя спортсмена слева до центра. """

        pos = self.frame_sportsman.place_info()
        x = float(pos['relx'])
        if x < 0.5:
            self.frame_sportsman.place(relx=x + 0.05)
            self.after(10, self.slide_position_sportsman)
        else:
            self.after(200, self.slide_position_total())
            self.slide_position_position()

    def slide_position_total(self):
        """ Перемещает итоговую оценку слева до центра. """

        pos = self.frame_total.place_info()
        x = float(pos['relx'])
        if x < 0.35:
            self.frame_total.place(relx=x + 0.05)
            self.after(10, self.slide_position_total)
        # else:
        #     self.slide_position_position()

    def slide_position_position(self):
        """ Перемещает позицию в турнире справа до центра. """

        pos = self.frame_position.place_info()
        x = float(pos['relx'])
        if x > 0.65:
            self.frame_position.place(relx=x - 0.05)
            self.after(10, self.slide_position_position)
        else:
            self.slide_position_points()

    def slide_position_points(self):
        """ Перемещает оценки слева до центра. """

        pos = self.frame_points.place_info()
        x = float(pos['relx'])
        if x < 0.5:
            self.frame_points.place(relx=x + 0.05)
            self.after(10, self.slide_position_points)



    # def slide_position_end(self):
    #     """ Перемещает текст с центра направо и удаляет. """
    #
    #     if self.frame_cup is not None:
    #
    #         pos = self.frame_cup.place_info()
    #         x = float(pos['relx'])
    #         if x < 1.3:
    #             self.frame_cup.place(relx=x + 0.05)
    #             self.after(10, self.slide_position_end)
    #
    #     self.frame_cup.destroy()
