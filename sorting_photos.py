from tkinter import *
import tkinter
from srt_photos_lgc import SP_logic
# import os
# from datetime import datetime


class Sorting_app(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title('Sorting Photos')
        self.geometry('485x150+500+200')
        self.resizable(False, False)
        # self.iconbitmap()
        self.set_ui()
        



    def set_ui(self):

        module = SP_logic()
        # label_result_text = module.execution(self)

        self.label_path = Label(self, text='Путь к папке сортировки').grid(row=0, column=0, columnspan=2)

        self.entry = Entry(self, width=60)
        self.entry.grid(row=1, column=0, padx=10)

        self.button_path = Button(self, text='Выбрать папку', command=lambda: module.btn_get_path(self))
        self.button_path.grid(row=1, column=1)

        self.button_main = Button(self, text='ВЫПОЛНИТЬ', bg='#6495ED', width=20, height=2, command=lambda: module.execution(self))
        self.button_main.grid(row=3, column=0, columnspan=2, pady=20)

        self.label_result = Label(self, text='')
        self.label_result.grid(row=4, column=0, columnspan=2, ipadx=30)

        




if __name__ == '__main__':
    root = Sorting_app()
    root.mainloop()