from tkinter import *
from tkinter import ttk

import tkinter as tk

from functions import sportsman_result, add_sportsman_table, delete_item_table, valid_entry_float, \
    validate_length, create_messages_text
from styles import style_container, style_entry_frame, style_entry, style_frame_label, frame_label_element, \
    style_button, style_button_special, style_table

TEST = "#fa552f"

FON_PANEL = "#4f6369"
FON_FIELD = "#364a4f"
FON_FIELD_MAP = "#cc6b41"
BORDER = "#00f4fc"
BORDER_RED = "#ba4216"
TEXT = "white"
ENTRY_BG = "#9dafb0"
ENTRY_TEXT = "#752502"
ENTRY_BG_FOCUSIN = "#c5d8d9"
SELECT_BG_MARKER = "#946a59" # выделение текста

FON_MENU = "#687375"
MARKER_MENU = "#e66b3e"
FON_TAB_ACTIVE = "#e66b3e"
FON_TAB_PRESSED = "#ba4216"

class PanelLeft(tk.Frame):
    """ Структура вкладки в блокноте. """

    def __init__(self, *args):
        super().__init__()


        self.configure(pady=10, bg=FON_PANEL)

        self.is_valid = (self.register(valid_entry_float), "%P")
        # self.is_valid_count = (self.register(validate_length), "%d", "%P", 12)

        self.point_1 = args[0]
        self.point_2 = args[1]
        self.point_3 = args[2]
        self.point_4 = args[3]
        self.point_5 = args[4]
        self.point_6 = args[5]
        self.point_penalty = args[6]
        self.total = args[7]

        self.popup = tk.Menu(self, tearoff=0, bg=FON_MENU, bd=0, activebackground=MARKER_MENU, activeborderwidth=3)
        self.popup.add_command(label="Посмотреть оценки", command=self.delete_sportsman)
        self.popup.add_command(label="Изменить", command=self.delete_sportsman)
        self.popup.add_command(label="На экран", command=self.delete_sportsman)
        self.popup.add_command(label="Трансляция", command=self.delete_sportsman)
        self.popup.add_separator()
        self.popup.add_command(label="Удалить", command=self.delete_sportsman)

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

        ####################

        self.container_cup = style_container(self.frame)
        self.container_cup.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.entry_frame_cup = style_entry_frame(self.container_cup, "Т у р н и р")
        self.entry_frame_cup.grid(row=0, column=1, columnspan=100, sticky="nsew", pady=10, padx=20)

        self.entry_cup = style_entry(self.entry_frame_cup)
        self.entry_cup.config(validate="key", validatecommand=(self.register(validate_length), "%d", "%P", 50))
        self.entry_cup.pack(fill=BOTH, pady=10, padx=10, expand=True)

        self.entry_frame_category = style_entry_frame(self.container_cup, "К а т е г о р и я")
        self.entry_frame_category.grid(row=1, column=1, columnspan=100, sticky="nsew", pady=10, padx=20)

        self.entry_category = style_entry(self.entry_frame_category)
        self.entry_category.config(validate="key", validatecommand=(self.register(validate_length), "%d", "%P", 45))
        self.entry_category.pack(fill=BOTH, pady=10, padx=10, expand=True)

        self.container_sportsman = style_container(self.frame)
        self.container_sportsman.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.entry_frame_sportsman = style_entry_frame(self.container_sportsman, "С п о р т с м е н / Д у э т")
        self.entry_frame_sportsman.grid(row=0, column=1, columnspan=100, sticky="nsew", pady=15, padx=20)

        self.entry_sportsman = style_entry(self.entry_frame_sportsman)
        self.entry_sportsman.config(validate="key", validatecommand=(self.register(validate_length), "%d", "%P", 30))
        self.entry_sportsman.pack(fill=BOTH, pady=10, padx=10, expand=True)

        self.frame_point = style_frame_label(self.container_sportsman, " Б а л л ы  з а  в ы с т у п л е н и е ")
        self.frame_point.grid(row=1, column=0, columnspan=100, sticky="nsew", pady=15, padx=30)

        self.frame_1 = frame_label_element(self.frame_point, self.point_1)
        self.frame_1.grid(row=0, column=0, pady=10, padx=5)
        self.entry_1 = style_entry(self.frame_1, point=self.point_1)
        self.entry_1.config(validate="key", validatecommand=self.is_valid)
        self.entry_1.pack()

        self.frame_2 = frame_label_element(self.frame_point, self.point_2)
        self.frame_2.grid(row=0, column=1, pady=10, padx=5)
        self.entry_2 = style_entry(self.frame_2, point=self.point_2)
        self.entry_2.config(validate="key", validatecommand=self.is_valid)
        self.entry_2.pack()

        self.frame_3 = frame_label_element(self.frame_point, self.point_3)
        self.frame_3.grid(row=0, column=2, pady=10, padx=5)
        self.entry_3 = style_entry(self.frame_3, point=self.point_3)
        self.entry_3.config(validate="key", validatecommand=self.is_valid)
        self.entry_3.pack()

        self.frame_4 = frame_label_element(self.frame_point, self.point_4)
        self.frame_4.grid(row=1, column=0, pady=10, padx=5)
        self.entry_4 = style_entry(self.frame_4, point=self.point_4)
        self.entry_4.config(validate="key", validatecommand=self.is_valid)
        self.entry_4.pack()

        self.frame_5 = frame_label_element(self.frame_point, self.point_5)
        self.frame_5.grid(row=1, column=1, pady=10, padx=5)
        self.entry_5 = style_entry(self.frame_5, point=self.point_5)
        self.entry_5.config(validate="key", validatecommand=self.is_valid)
        self.entry_5.pack()

        self.frame_6 = frame_label_element(self.frame_point, self.point_6)
        self.frame_6.grid(row=1, column=2, pady=10, padx=5)
        self.entry_6 = style_entry(self.frame_6, point=self.point_6)
        self.entry_6.config(validate="key", validatecommand=self.is_valid)
        self.entry_6.pack()

        self.frame_7 = frame_label_element(self.frame_point, self.point_penalty)
        self.frame_7.grid(row=2, column=0, columnspan=2, pady=10, padx=5)
        self.entry_7 = style_entry(self.frame_7, point=self.point_penalty)
        self.entry_7.config(validate="key", validatecommand=self.is_valid)
        self.entry_7.pack()

        self.frame_total = frame_label_element(self.frame_point, self.total)
        self.frame_total.grid(row=2, column=1, columnspan=2, pady=10, padx=5)
        self.entry_total = style_entry(self.frame_total)
        self.entry_total.config(validate="key", validatecommand=self.is_valid)
        self.entry_total.pack()

        """ для общего балла переводим значение во float """
        # self.num1 = tk.StringVar()
        # self.total = ttk.Label(self.frame_total, text="ФО :", background="#cbeef5")
        # self.total.pack(side=LEFT)
        # self.entry_total = ttk.Entry(self.frame_total, textvariable=self.num1, width=7, justify=CENTER)
        # self.entry_total.pack(fill=X, anchor="center")

        self.button_clear = style_button_special(self.container_sportsman, "Сбросить", self.click_button_clear)
        self.button_clear.grid(row=3, column=6, pady=10, padx=0)

        self.button_sportsman_tv = style_button_special(self.container_sportsman, "Трансляция", self.click_button_clear)
        self.button_sportsman_tv.grid(row=3, column=50, pady=10, padx=0)

        self.button_apply = style_button_special(self.container_sportsman, "На экран", self.click_button_apply)
        self.button_apply.grid(row=3, column=94, pady=10, padx=0)

        self.frame_table = style_container(self.frame)
        # self.frame_table.configure(highlightcolor=BORDER_RED,)



        self.frame_table.pack(side=TOP, fill=X, pady=5, padx=10, anchor="n", expand=True)

        self.title_frame_table = ttk.Label(self.frame_table, text="Т у р н и р н а я   т а б л и ц а",
                                           background=FON_FIELD, foreground=BORDER)
        self.title_frame_table.pack(side=TOP, pady=5, padx=10, anchor="n", expand=True)

        self.title_frame_table = ttk.Label(self.frame_table, text=f"(по категории)",
                                           background=FON_FIELD, foreground=BORDER)
        self.title_frame_table.pack(side=TOP, pady=1, padx=10, anchor="n", expand=True)

        # Создание таблицы:
        self.list = []
        for arg in args[:7]:
            if len(arg) > 0:
                self.list.append(arg)

        self.table_columns = ("place", "athlete", "total",) + tuple(self.list)  # определяем столбцы
        self.table_style = style_table(self.frame_table)  # определяем стиль таблицы
        self.table = ttk.Treeview(self.frame_table, columns=self.table_columns, show='headings',
                                  padding=6, height=10, selectmode="browse")  # browse - только одно выделение в табл.
        self.table.bind('<Double-Button-1>', self.selectItem)
        # self.table.bind("<Button-3>", self.popup_list)
        self.table.bind("<<TreeviewSelect>>", self.button_popup_list)
        self.table.pack(side=TOP, fill=BOTH, pady=25, padx=30, anchor="n", expand=True)

        # определяем заголовки:
        self.table.heading("place", text="Место")
        self.table.heading("athlete", text="Спортсмен/дуэт")
        self.table.heading("total", text=self.total)

        # настраиваем колонки:
        self.table.column("#1", anchor="center", minwidth=50, width=50, stretch=False)
        self.table.column("#2", anchor="center", minwidth=150, width=150, stretch=True)
        self.table.column("#3", anchor="center", minwidth=50, width=50, stretch=False)

        # добавляем дополнительные колонки с заголовками в зависимости от количества оценок:
        self.count = 3
        for element_list in self.list:
            self.count += 1

            self.table.heading(str(element_list), text=element_list)
            self.table.column(f"#{self.count}", anchor="center", minwidth=40, width=50, stretch=False)

        self.table_cleaner_button = style_button(self.frame_table, "Очистить", self.cleaner_table)
        self.table_cleaner_button.pack(side=LEFT, anchor="w", padx=45, pady=10, expand=True)

        self.button_delete_sportsman = style_button(self.frame_table, "Трансляция", None)
        self.button_delete_sportsman.pack(side=LEFT, anchor="w", padx=45, pady=10, expand=True)

        self.button_show_table = style_button(self.frame_table, "На экран", None)
        self.button_show_table.pack(side=TOP, anchor="e", padx=45, pady=10, expand=True)

        self.button_delete_tab = style_button(self.frame, "Удалить панель", self.delete_tab)
        self.button_delete_tab.pack(side=TOP, pady=5, padx=10, anchor="sw", expand=True)

    def button_popup_list(self, event):
        """ Устанавливает для выделенной строки в таблице функцию-обработчик 'правый клик' мыши. """

        for selected_item in self.table.selection():
            # item = table.item(selected_item)
            # self.table.delete(selected_item)

            self.table.bind("<Button-3>", self.popup_list)

    def popup_list(self, event):
        """ Открывает всплывающий список. """

        try:
            self.popup.selection = self.table.set(self.table.identify_row(event.y))
            self.popup.post(event.x_root, event.y_root)
        finally:
            # make sure to release the grab (Tk 8.0a1 only)
            self.popup.grab_release()

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

    def selectItem(self, event):
        """ Снимает выделение со строки таблицы. """

        for selected_item in self.table.selection():
            # item = table.item(selected_item)
            self.table.selection_remove(selected_item)

    def click_button_apply(self):
        """ Проверяет заполнение нужных entry.
        Передает спортсмена и его результаты в таблицу.
        Передает спортсмена и его результаты для вывода на экран. """

        if self.entry_sportsman.get() is not None and len(self.entry_sportsman.get()) != 0:
            if self.entry_total.get() is not None and len(self.entry_total.get()) != 0:


                add_sportsman_table(self.table, self.entry_sportsman.get().title(), self.entry_total.get())


                sportsman_result(self.table, self.entry_cup.get(), self.entry_category.get(), self.entry_sportsman.get(),
                                 self.entry_1.get(), self.entry_2.get(), self.entry_3.get(), self.entry_4.get(),
                                 self.entry_5.get(), self.entry_6.get(), self.entry_7.get(), self.entry_total.get())
            else:
                create_messages_text(f"Отсутствует значение итоговой оценки", False)
        else:
            create_messages_text(f"Не указано имя спортсмена", False)

        # self.click_button_clear() # нужно ли сразу очищать ?

    def click_button_clear(self):
        """ Очищает данные в полях ввода. """

        self.entry_sportsman.delete(0, END)
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_5.delete(0, END)
        self.entry_6.delete(0, END)
        self.entry_7.delete(0, END)
        self.entry_total.delete(0, END)

    def delete_sportsman(self):
        """ Устанавливает для выделенной строки в таблице функцию-обработчик, которая удаляет выделенную строку. """

        delete_item_table(self.table)

    def cleaner_table(self):
        """ Очищает таблицу. """

        self.table.delete(*self.table.get_children())
        create_messages_text(f"Таблица успешно очищена")

    def delete_tab(self):
        """ Удаляет текущую вкладку. """

        self.destroy()
        create_messages_text(f"Вкладка успешно удалена")
