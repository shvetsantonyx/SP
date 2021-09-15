from tkinter.constants import END
from tkinter import filedialog, messagebox
import os.path
import time
import shutil


class SP_logic:

    def __init__(self):

        self.result = False

    # кнопка "выбрать путь"
    def btn_get_path(self, tkinter):
        direction_main_path = filedialog.askdirectory()
        
        tkinter.entry.insert(0, direction_main_path)

        tkinter.label_result['text'] = ''
        defaultbg = tkinter.cget('bg')
        tkinter.label_result['bg'] = defaultbg

    # кнопка "ВЫПОЛНИТЬ"
    def execution(self, tkinter):

        entry_path = tkinter.entry.get()

        if entry_path == '':
            tkinter.label_result['text'] = 'Выберите папку!'
            tkinter.label_result['bg'] = '#B22222'
        
        main_path = os.walk(entry_path)

        for element in main_path:
            # print(element)
            # print(element[2])
            for file_name in element[2]:
                # print(file_name)
                if '.bmp' in file_name or '.jpeg' in file_name or '.jpg' in file_name:
                    try:
                        # создание имени директории
                        dir_name = time.strftime('%d_%m_%Y', time.gmtime(os.path.getmtime((entry_path + '\\' + file_name))))

                        file_new_path = entry_path + '\\' + file_name # для нового пути файла
                        new_dir_path = entry_path + '\\' + dir_name # путь для новой директории

                        # print(file_new_path)
                        # print(new_dir_path)
                        # print(dir_name)

                    except: FileNotFoundError

                    
                    folder = os.listdir(path=entry_path)

                    try:
                        if dir_name in folder:
                            try:
                                shutil.move(file_new_path, new_dir_path)
                                self.result = True
                            except: shutil.Error
                        else:          
                            os.mkdir(new_dir_path)
                            shutil.move(file_new_path, new_dir_path)
                            self.result = True
                    except: UnboundLocalError

        tkinter.entry.delete(0, END)

        # печать вывода результата
        if self.result == True:
            tkinter.label_result['text'] = 'Сортировка выполнена успешно!'
            tkinter.label_result['bg'] = '#00FA9A'
            self.result = False

    # кнопка инфо
    def btn_info(self):
        messagebox.showinfo(title='Info', message='Данная программа сортирует фото в папки \
по дате модификации/создания файлов.\
 Для этого вставьте путь в поле ввода или выберите исходную папку через проводник и нажмите кнопку "ВЫПОЛНИТЬ".')
            