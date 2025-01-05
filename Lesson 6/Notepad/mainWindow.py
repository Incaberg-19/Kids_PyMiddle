import tkinter as tk
from tkinter import scrolledtext, filedialog # импортируем доп. модули из библиотеки

class MainWindow(tk.Tk): # Tk главный класс в котором находится наше окно
    # мы наследуем от этого класса его атрибуты и методы.
    def __init__(self):
        super().__init__() # и инициализируем всё что было в инициализации род. класса
        # super - обращение к родительскому атрибуту/методу
        self.title("Блокнот")
        self.geometry("800x600")
        # размеры 96 по ширине и 37 по высоте, это оптимальные размеры для окна 800 х 600. 
        self.edit_text = scrolledtext.ScrolledText(width=96, height=37)
        # виджет ScrolledText - это многостраничное текстовое поле с прокруткой.
        self.edit_text.pack()
        self._create_menu()

        
    def _create_menu(self):
        self._menu = tk.Menu(self,tearoff=0)
        # создали класс menu. С помощью него можно создать кнопки сверху.
        # Menu используется для создания меню-бара в верхней части окна.
        self._menu.add_command(label="Открыть файл", command=self._open_file)
        self._menu.add_command(label="Сохранить файл как", command=self._save_file_as)
        self._menu.add_command(label="Сохранить файл", command=self._save_file)
        self._menu.add_command(label="О программе", command=self._open_about)
        self.config(menu=self._menu)


    '''
    filedialog.askopenfilename() вызывает проводник (или эквивалент в зависимости от операционной системы) для выбора файла. Вот ключевые моменты:
    filedialog.askopenfilename() открывает стандартное диалоговое окно выбора файла.
    Она позволяет пользователю выбрать существующий файл или указать путь к новому файлу.
    Функция возвращает путь к выбранному файлу как строку.
    '''

    def _open_file(self):
        self._filepath = filedialog.askopenfilename() # открываем проводник
        if self._filepath != "": # если вернувшийся путь не пустой
            with open(self._filepath, "r",encoding='utf-8') as file:
                # открыть этот путь как файл и прочитать его
                text = file.read()
                self.title(f"Блокнот {file.name}") # изменить название окна под путь файла
                 # Эта строка очищает все содержимое текстового поля которое было
                self.edit_text.delete("1.0", tk.END) 
                # Эта строка вставляет всё содержимое файла в текущее текстовое поле
                self.edit_text.insert("1.0", text)
    
    def _save_file_as(self):
        self._filepath = filedialog.asksaveasfilename() # открываем проводник
        # чтобы сохранить путь файла
        self._save_file() # вызываем метод сохрания файла (по полученному пути)

    def _save_file(self):
        if self._filepath != "": # если путь файла не пустой
            text = self.edit_text.get("1.0", tk.END) # получить всё то что мы
            # написали в текстовом окне
            with open(self._filepath, "w",encoding='utf-8') as file:
                # записываем файл по пути
                file.write(text)
        else:
            self._save_file_as() # если путь пустой то вызываем проводник
            # и просим пользователя указать путь сохранения

    def _open_about(self):
        self.help_window = tk.Toplevel(self)
        # Используем tk.Toplevel для создания второго окна (всплывающего окна)
        self.help_window.title("Справка")
        self.help_window.geometry("800x150")
        intro = 'Инструкция по использованию'
        openButtonInfo = 'Кнопка \"Открыть файл\" вызывает проводник где пользователю предлагается найти текстовый файл и открыть его.\nСодержимое будет выведено на экран.'
        saveButtonInfoAs = 'Кнопка \"Сохранить файл как\" вызывает проводник где пользователю предлагается указать место сохранения файла.'
        saveButtonInfo = 'Кнопка \"Сохранить файл\" либо сохраняет файл по текущему пути если таков существует, либо активирует кнопку  \"Сохранить файл как\".'
        help_label = tk.Label(self.help_window, text=f"{intro}\n{openButtonInfo}\n{saveButtonInfoAs}\n{saveButtonInfo}", justify=tk.LEFT)
        help_label.pack(pady=15)

        close_button = tk.Button(self.help_window, text="Закрыть", command=self.help_window.destroy)
        close_button.pack()