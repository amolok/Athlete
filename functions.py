import re
from tkinter import *

from windows import Athlete

athlete_window = None
# scoreboard_window = None
in_object = None
in_admin_right = None

count = 0

ENTRY_BG = "#9dafb0"
TABLE_BG = "#f5b39a"
TABLE_BG_END = "#e66b3e"
TABLE_TEXT = "black"
TABLE_TEXT_END = "white"

BORDER = "#00f4fc"
RED = "#ba4216"
GRAY = "#364a4f"


def check_athlete_window():
    """ Проверяет, открыто ли окно Атлет. """

    global athlete_window
    if athlete_window is None:
        create_messages_text("Окно Атлет не создано", False)
        return False
    else:
        return True


def transfer_object(admin_left):
    """ Принимает левую админку, как объект класса, и записывает ее в переменную. """

    global in_object
    in_object = admin_left
    # print(f"Функция {transfer_object} запущена")


def transfer_admin_right(admin_right):
    """ Принимает правую админку, как объект класса, и записывает ее в переменную. """

    global in_admin_right
    in_admin_right = admin_right
    # print(f"Функция {transfer_admin_right} запущена")


def create_messages_text(text, color=True):
    """ Формирует текст уведомления.
    Вызывает функцию создания уведомления, передает текст. """

    global count
    count += 1
    in_text = f" {count}.  {text}\n"
    in_admin_right.right_tools.messages_text(in_text, color)


def click_create_panel(title, point_1, point_2, point_3, point_4, point_5, point_6, point_penalty, total):
    """ Добавляет новую панель в левой админке. """

    global in_object
    in_object.panel_left(title, point_1, point_2, point_3, point_4, point_5, point_6, point_penalty, total)
    create_messages_text(f"Вкладка '{title.upper()}' для управления оценками успешно создана")

###############################


def click_create_athlete(entry_city, entry_year):
    """ Создает окно Атлет в глобальную переменную.
    Переопределяет нажатие 'Х' в углу окна на функцию 'close_athlete'. """

    global athlete_window
    athlete_window = Athlete(entry_city, entry_year)
    athlete_window.protocol("WM_DELETE_WINDOW", athlete_window.close_athlete)
    create_messages_text(f"Окно Атлет открыто")


def fullscreen_athlete():
    """ Разворачивает окно 'Атлет' в полный экран. """

    global athlete_window
    if not check_athlete_window():
        pass
    elif athlete_window.state is False:
        athlete_window.attributes("-fullscreen", True)
        athlete_window.state = True
        create_messages_text(f"Окно Атлет переведено в полноэкранный режим ")
    else:
        athlete_window.attributes("-fullscreen", False)
        athlete_window.state = False
        create_messages_text(f"Окно Атлет переведено в режим окна")


def validate_length(action, value_if_allowed, count):
    """ Валидация поля ввода на количество знаков. """

    if action == "1":
        return len(value_if_allowed) <= int(count)
    return True


def valid_entry_float(P):
    """ Валидация поля ввода на соответствие float. """

    if P:
        try:
            float(P)  # Проверяет, является ли %P значением с плавающей запятой
        except ValueError:  # Не принимает вводимые пользователем данные, если они не соответствуют
            return False
    return True  # Обратить внимание, что при этом все введенные данные не будут считаться действительными (???)

    # Следующий вариант также валидирует, но исключает возможность очищения поля entry:
    # return re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$', newval) is not None


def sportsman_result(table, cup, category, sportsman, entry_1, entry_2, entry_3,
                     entry_4, entry_5, entry_6, entry_7, entry_total):
    """ Принимает данные и выводит их на окно Атлет. """

    # global athlete_window
    global in_admin_right
    if check_athlete_window():
        athlete_window.create_sportsmen()
        sportsmen_position = None
        for k in table.get_children(""):
            if table.set(k, 1).upper() == sportsman.upper():
                sportsmen_position = table.set(k, 0)
                # print(f"Значение {table.set(k, 0)} совпало")
            # else:
                # print(f"Значение {sportsman} с таблицей НЕ совпало")

        # sportsmen_position = table.#1[sportsman]
        # sportsmen_position = table.set(sportsman, 2)

        athlete_window.athlete_sportsmen.result_sportsmen(cup, category, sportsman, entry_1, entry_2,
                                                          entry_3, entry_4, entry_5, entry_6, entry_7, entry_total,
                                                          sportsmen_position)
        create_messages_text(f"Спортсмен '{sportsman.title()}' успешно создан")


def click_wallpaper():
    """ Переключает на экран Слайд-шоу. """

    global athlete_window
    if check_athlete_window():
        athlete_window.switch_wallpaper()
        create_messages_text(f"В окне Атлет запущен показ слайдов")

######################################


# def change_color_button_red(button):
#     """ Меняет цвет кнопки. """
#
#     print(type(button))
#     # button.configure(bordercolor=RED)
#     button.style.configure("MyButton.TButton", bordercolor=RED)
#
#
# def change_color_button_gray(button):
#     """ Заменяет цвет кнопки на исходный. """
#
#     # button.configure(background=GRAY)
#     pass
#
# def change_color_button_back(button):
#     """ Заменяет цвет кнопки на исходный. """
#
#     # button.configure(background=BORDER)
#     pass
#
# def blink_button(button):
#     """  """
#
#     change_color_button_red(button)
#     button.after(120, change_color_button_gray, button)
#     button.after(240, change_color_button_red, button)
#     button.after(360, change_color_button_gray, button)
#     button.after(480, change_color_button_red, button)
#     button.after(600, change_color_button_back, button)


def table_color(table, tag):
    """ Меняет цвет строки в таблице. """

    table.tag_configure(tag, background=TABLE_BG, foreground=TABLE_TEXT)


def table_color_back(table, tag):
    """ Заменяет цвет строки в таблице на исходный. """

    table.tag_configure(tag, background=TABLE_BG_END, foreground=TABLE_TEXT_END)


def sportsman_location(table):
    """ Определяет позицию (место) спортсмена в турнирной таблице. """

    value = 0
    for k in table.get_children(""):
        value += 1
        table.set(k, 0, value)


def table_sort(col, reverse, table, sportsman=None):
    """ Сортирует спортсменов в таблице по убыванию итоговой оценки.
    Вызывает функцию определения позиции спортсмена.
    Вызывает функции смены цветов, эффект мигания. """

    # получаем все элементы (все строки) с помощью идентификатора (k),
    # из каждого элемента создаем кортеж, в котором итоговая оценка и идентификатор элемента,
    # создаем список из кортежей
    list_sort = [(table.set(k, col), k) for k in table.get_children("")]
    # сортируем список по итоговой оценке
    list_sort.sort(key=lambda t: float(t[0]), reverse=reverse)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(list_sort):
        table.move(k, "", index)

    # table.heading(col, command=lambda c=col: table_sort(c, not reverse, table))

    sportsman_location(table)


    # мигающий цвет строки
    if sportsman is not None:
        table_color(table, sportsman)
        table.after(120, table_color_back, table, sportsman)
        table.after(240, table_color, table, sportsman)
        table.after(360, table_color_back, table, sportsman)
        table.after(480, table_color, table, sportsman)
        table.after(3500, table_color_back, table, sportsman)


def add_sportsman_table(table, sportsman, total):
    """ Добавляет спортсмена в таблицу. Вызывает функцию сортировки таблицы. """

    data_sportsman = [
        (
            None,
            sportsman,
            float(total),
        )
    ]

    for element in data_sportsman:
        table.insert("", END, values=element,  tags=(sportsman, float(total),))

    table_sort("#3", True, table, sportsman)


def delete_item_table(table):
    """ Удаляет выделенную строку в таблице. Вызывает функцию сортировки таблицы. """

    for selected_item in table.selection():
        # item = table.item(selected_item)
        table.delete(selected_item)
    table_sort("#3", True, table)


# def cleaner_table(table):
#     """ Очищает таблицу. """
#
#     print("Запущено очищение таблицы")
#
#     print(*table.get_children())
#     table.delete(*table.get_children())