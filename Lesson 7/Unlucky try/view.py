import tkinter as tk
# class Menu:

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Заметки")
        self.geometry("800x600") 

        self.root = tk.Frame(self,bg="gray",width=800,height=600) # создание второго основного окна
        self.root.pack()
        '''
        чтобы посмотреть в какую область распаковывается можно использовать bg="pink"
        Когда вы создаете холст внутри определенного фрейма, холст не автоматически принимает
        все доступное пространство фрейма. Вместо этого:
        1. Холст по умолчанию имеет минимальные размеры.
        2. Фактический размер холста определяется путем размещения его внутри фрейма. НО
        ЭТО РАБОТАЕТ ТОЛЬКО ЕСЛИ МЫ НЕ УКАЗАЛИ width=800, height=600
        '''

        self.scrollBar = tk.Scrollbar(self.root , orient='vertical') # создание скроллбара в root

        self.canvas = tk.Canvas(self.root,width=750,height=550,bg='white') 
        # создание canvas (только его можно скроллбарить)
        self.canvas.configure(yscrollcommand=self.scrollBar.set) # связывание canvas и скроллбара

        self.canvas.place(relx=0.49, rely=0.5, anchor="c") # установка расположения
        self.scrollBar.place(relx=0.977, rely=0.5, anchor="c",relheight=0.925) # установка расположения

        # Использование place() вместо pack() для внутреннего фрейма чтобы
        # избежать поведения, когда один фрейм "затопляет" другой при использовании pack()
        # self.canvas.pack(fill='both', expand=True)
        self.button_container = tk.Frame(self.canvas,width=750,height=550) # создание в canvas области для кнопок
        
        self.canvas.create_window((0, 0), window=self.button_container, anchor='nw',width=750,height=550) # пихаем эту область на экран
        for c in range(3): self.button_container.columnconfigure(index=c, weight=1)
        for r in range(100): self.button_container.rowconfigure(index=r, weight=1)
        # self.button_container.grid_propagate(False)
        self.add_buttons() # вызов создания кнопок
        
        # Обработка изменения размера
        # self.button_container.bind("<Configure>", self.on_frame_configure) # без этой строчки прокрутся невозможна
        '''
        Эта строка устанавливает обработчик события для button_container. Когда размер button_container изменяется
        (например, при добавлении новых кнопок или изменении их размеров), вызывается метод on_frame_configure.
        Это необходимо для обновления области прокрутки, так как размер содержимого влияет на то, какая часть его будет видима в canvas.
        '''
        # self.scrollBar.config(command=self.canvas.yview)
        '''
        Эта строка связывает вертикальный ползунок (scrollBar) с вертикальным представлением canvas.
        Это означает, что когда пользователь перемещает ползунок, область видимости canvas будет изменяться
        в соответствии с положением ползунка. 
        '''
        
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        '''
        В этом методе обновляется свойство scrollregion для canvas. Метод bbox("all") возвращает размеры области,
        занимаемой всеми видимыми элементами внутри canvas (в данном случае, это размер button_container).
        Установка scrollregion позволяет canvas знать, какова полная область, которую необходимо прокручивать.
        Если размеры элементов изменятся (например, добавится новая кнопка), и scrollregion не будет обновлен,
        ползунок может не работать корректно, и вы не сможете прокручивать до новых элементов.
        '''

    def add_buttons(self):
        for row in range(100):
            frame = tk.Frame(self.button_container)
            frame.grid(row=row, column=0, sticky="ew")  # Размещаем фрейм в первой колонке
            
            for col in range(3):
                btn = tk.Button(frame, text=f"({row},{col})", padx=10, pady=5)  # Добавляем отступы вокруг текста
                btn.grid(row=0, column=col, sticky="nsew")  # Распределяем кнопку по всей ширине фрейма
                
                # Настройка ширины колонки
                frame.grid_columnconfigure(col, weight=1)
                
        # self.button_container.grid_rowconfigure(0, weight=1)
        # self.button_container.grid_columnconfigure(0, weight=1)


# Запуск приложения
app = View()
app.mainloop()