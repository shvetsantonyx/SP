from tkinter import *
from srt_photos_lgc import SP_logic



class Sorting_app(Tk):


    def __init__(self):

        Tk.__init__(self)

        self.title('PhotoSort SAI')
        self.geometry('485x150+500+200')
        self.resizable(False, False)
        self.iconbitmap('icon.ico')

        self.set_ui()
        

    def set_ui(self):

        module = SP_logic()

        self.label_path = Label(self, text='Путь к папке сортировки').grid(row=0, column=0, columnspan=3)

        self.entry = Entry(self, width=60)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10)

        self.button_path = Button(self, text='Выбрать папку', command=lambda: module.btn_get_path(self))
        self.button_path.grid(row=1, column=2)

        self.button_main = Button(self, text='ВЫПОЛНИТЬ', bg='#6495ED', width=20, height=2, command=lambda: module.execution(self))
        self.button_main.grid(row=3, column=1, padx=20, pady=20)

        self.label_result = Label(self, text='')
        self.label_result.grid(row=4, column=1, ipadx=30)

        self.button_info = Button(self, text='?', font=15, width=3, command=module.btn_info)
        self.button_info.place(x=10, y=110)
        

if __name__ == '__main__':
    root = Sorting_app()
    root.mainloop()
    