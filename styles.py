from tkinter import *
from tkinter import ttk, scrolledtext
import tkinter as tk

FON_PANEL = "#4f6369"
FON_FIELD = "#364a4f"
FON_FIELD_MAP = "#cc6b41"
FON_ENTRY_FIELD = "#364a4f"

BORDER = "#00f4fc"
TEXT = "white"

ENTRY_BG = "#9dafb0"
ENTRY_BG_FOCUSIN = "#b6edf0"
ENTRY_TEXT_BEFORE = "#5e6d6e"
ENTRY_TEXT = "#2a393d"
ENTRY_TEXT_AFTER = "#014145"

# SELECT_BG = "#946a59"  # выделение текста
BUTTON_BG = "#2a393d"
BUTTON_BORDER = "#ba4216"
BUTTON_BG_PRESSED = "#57463f"
BUTTON_BORDER_SPECIAL = "#05e4fc"
BUTTON_BG_PRESSED_SPECIAL = "#1e4f52"
BUTTON_BG_ACTIVE = "#4f6369"

# BUTTON_BORDER_SCREEN = "#07f0ae" # цвет для общих кнопок

SELECT_BG_MARKER = "#946a59"  # выделение текста

FON = "#687375"
TAB = "#687375"
TAB_MAP = "#4f6369"
TEXT_2 = "#00f4fc"

TABLE_BG = "#e66b3e"
TABLE_TEXT = "#ba02cf"
TABLE_HEADING = "#ba4216"

FON_TAB_PRESSED = "#ba4216"

def style_notebook(frame):
    """ Стилизует блокнот для левой и правой частей административной панели. """

    style = ttk.Style(frame)
    style.theme_use("clam")
    style.layout("TNotebook", [])
    style.configure("TNotebook", borderwidth=0)
    style.configure("Left.TNotebook", background=FON)
    style.configure("Right.TNotebook", background=FON, tabposition='ne')
    style.configure("TNotebook.Tab", background=TAB, foreground=TEXT)
    style.map("TNotebook.Tab",
              focuscolor=style.configure(".")["background"],  # цвет пунктирной обводки как у фона
              background=[("selected", TAB_MAP), ("active", TAB_MAP)],
              foreground=[("selected", TEXT_2), ("active", TEXT_2)]
              )


def style_container(panel):
    """ Возвращает стилизованный контейнер. """

    for c in range(100): panel.columnconfigure(index=c, weight=1)
    for r in range(100): panel.rowconfigure(index=r, weight=1)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Style.TFrame", background=FON_FIELD, relief=SOLID, bordercolor=BORDER, borderwidth=2)

    container = ttk.Frame(panel, style="Style.TFrame")
    return container


def style_frame_label(frame, text):
    """ Возвращает стилизованную рамку LabelFrame. """

    frame_point = tk.LabelFrame(frame, labelanchor="n", text=text, font="Arial 8 bold",
                                bg=FON_FIELD, fg=TEXT_2, borderwidth=1, relief=RAISED, padx=10, pady=15)
    return frame_point


def invisible_frame(frame):
    """ Возвращает невидимую рамку. """

    frame = tk.Frame(frame, bg=FON_FIELD, borderwidth=0, relief=RIDGE)
    return frame


def style_entry_frame(container, text, pady=15, padx=10):
    """ Возвращает стилизованную рамку для ввода текста с названием рамки (label). """

    for c in range(100): container.columnconfigure(index=c, weight=1)
    for r in range(100): container.rowconfigure(index=r, weight=1)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("MyStyle.TFrame", background=FON_ENTRY_FIELD, relief=RAISED, borderwidth=0)

    entry_container = ttk.Frame(container, style="MyStyle.TFrame")

    label = ttk.Label(entry_container, text=text, background=FON_ENTRY_FIELD, foreground=TEXT)
    label.pack(side=LEFT, fill=BOTH, pady=pady, padx=padx)

    return entry_container


def frame_label_element(frame, text):
    """ Возвращает стилизованную рамку ввода одной оценки для левой панели с названием рамки (label). """

    for c in range(4): frame.columnconfigure(index=c, weight=1)
    for r in range(3): frame.rowconfigure(index=r, weight=1)

    element = tk.Frame(frame, bg=FON_FIELD, borderwidth=0, relief=RIDGE, padx=10, pady=5)
    label = tk.Label(element, text=text, background=FON_FIELD, foreground=TEXT, relief=SOLID, anchor=CENTER,
                     width=7, height=1, bd=0)
    label.pack(side=LEFT, padx=5)
    # entry = style_entry(element)
    # entry.pack()
    return element


def style_entry(frame, width=7, point=None):
    """ Возвращает стилизованное поле для ввода. """

    state = NORMAL
    if point is not None and len(point) == 0:
        state = DISABLED

    entry = tk.Entry(frame, font="Arial 11 bold", justify=CENTER, bd=1, relief=SOLID, bg=ENTRY_BG,
                     fg=ENTRY_TEXT_BEFORE, selectbackground=SELECT_BG_MARKER, takefocus=True,
                     width=width, state=state)
    entry.config(disabledbackground=FON_FIELD)

    entry.bind('<FocusIn>', lambda e: entry.config(bg=ENTRY_BG_FOCUSIN, fg=ENTRY_TEXT))
    entry.bind('<FocusOut>', lambda n: entry.config(bg=ENTRY_BG, fg=ENTRY_TEXT_AFTER))

    return entry


def style_button(frame, text, command):
    """ Возвращает стилизованную кнопку с названием кнопки. """

    # state = NORMAL
    # if athlete_window is None:
    #     state = DISABLED

    for c in range(4): frame.columnconfigure(index=c, weight=1)
    for r in range(3): frame.rowconfigure(index=r, weight=1)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("MyButton.TButton", background=BUTTON_BG, foreground=TEXT, relief=SOLID,
                    bordercolor=BUTTON_BORDER, borderwidth=1)
    style.map("MyButton.TButton",
              focuscolor=style.configure(".")["background"],  # цвет пунктирной обводки как у фона
              background=[("pressed", BUTTON_BG_PRESSED), ("active", BUTTON_BG_ACTIVE)],
              foreground=[("pressed", TEXT), ("active", TEXT)]
              )
    button = ttk.Button(frame, text=text, style="MyButton.TButton", command=command, width=15)
    return button


def style_button_special(frame, text, command):
    """ Возвращает стилизованную кнопку с названием кнопки. """

    for c in range(4): frame.columnconfigure(index=c, weight=1)
    for r in range(3): frame.rowconfigure(index=r, weight=1)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("SpecialButton.TButton", background=BUTTON_BG, foreground=TEXT, relief=SOLID,
                    bordercolor=BUTTON_BORDER_SPECIAL, borderwidth=1)
    style.map("SpecialButton.TButton",
              focuscolor=style.configure(".")["background"],  # цвет пунктирной обводки как у фона
              background=[("pressed", BUTTON_BG_PRESSED_SPECIAL), ("active", BUTTON_BG_ACTIVE)],
              foreground=[("pressed", TEXT), ("active", TEXT)]
              )

    button = ttk.Button(frame, text=text, style="SpecialButton.TButton", command=command, width=15)

    return button


def style_table(frame):
    """ Возвращает новый стиль для таблицы.
    Fix проблемы с цветами в строках таблицы. """

    table_style = ttk.Style(frame)
    table_style.theme_use("clam")
    table_style.map('Treeview',
                    foreground=[elm for elm in table_style.map('Treeview', query_opt='foreground')
                                if elm[:2] != ('!disabled', '!selected')],
                    background=[elm for elm in table_style.map('Treeview', query_opt='background')
                                if elm[:2] != ('!disabled', '!selected')],
                    )
    table_style.configure("Treeview", font=("Arial", 10), background=TABLE_BG, rowheight=15, fieldbackground=TABLE_BG,
                          foreground=TABLE_TEXT, bordercolor=BUTTON_BORDER)
    table_style.configure("Treeview.Heading", font=("Arial", 10), background=TABLE_HEADING, foreground=TEXT)

    # Настройка чередующихся цветов строк
    # tree.tag_configure('oddrow', background='#E8E8E8')
    # tree.tag_configure('evenrow', background='#FFFFFF')
    #
    # # Добавление данных с чередующимися цветами строк
    # for i in range(len(data)):
    #     if i % 2 == 0:
    #         table.insert(parent='', index=i, values=data[i], tags=('evenrow',))
    #     else:
    #         table.insert(parent='', index=i, values=data[i], tags=('oddrow',))

    return table_style


def style_scrolled_text():
    """  """

    style = ttk.Style()
    style.theme_use('clam')  # Ensure theme supports customization
    style.configure("Custom.Vertical.TScrollbar",
                    troughcolor=FON_PANEL,
                    bordercolor=FON_PANEL,
                    width=5,
                    # background=FON_FIELD,
                    # activebackground=TEST,
                    # background=FON_TAB,
                    # borderwidth=0,
                    # elementborderwidth=0,
                    # highlightcolor=FON_FIELD,
                    # highlightthickness=1,
                    # highlightbackground=TEST,
                    # relief="sunken",
                    )
    style.map('TScrollbar',
              background=[('!active', FON_FIELD),
                          ('pressed', FON_TAB_PRESSED),
                          ('active', FON_TAB_PRESSED)
                          ],
              # foreground=[('!active', TEST),
              #             ('pressed', TEST),
              #             ('active', BORDER)
              #             ],
              )


