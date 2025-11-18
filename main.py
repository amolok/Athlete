from tkinter import *
from tkinter import ttk
import tkinter as tk

from admin_panel import AdminLeft, AdminRight
from functions import transfer_object, transfer_admin_right
from windows import Admin

FON = "#687375"
FON_PANEL = "#4f6369"
TAB = "#687375"
TAB_MAP = "#4f6369"
BORDER = "#00f4fc"
TEXT = "white"
TEXT_2 = "#00f4fc"


admin_panel = Admin()


admin_left = AdminLeft(admin_panel, style="Left.TNotebook")
admin_left.place(relx=0.25, rely=0.5, anchor=CENTER, relwidth=0.47, relheight=0.97)
transfer_object(admin_left)



###########################

admin_right = AdminRight(admin_panel, style="Right.TNotebook")
admin_right.place(relx=0.75, rely=0.5, anchor=CENTER, relwidth=0.47, relheight=0.97)
transfer_admin_right(admin_right)
#
# frame_11 = PanelRightTools(admin_right)
# frame_22 = PanelRight(admin_right)
#
# frame_11.pack()
# frame_22.pack()
#
# admin_right.add(frame_11, text="Инструменты")
# admin_right.add(frame_22, text="Панель 2")


if __name__ == '__main__':

    admin_panel.mainloop()


