import tkinter as tk

class mainWindow(tk.Tk):
    def __init__(self,process_btn):
        super().__init__()
        self.title("Заметки")
        self.geometry("800x600") 

        self.process_btn = process_btn


        self.root = tk.Frame(self,bg="gray",width=800,height=600) # создание второго основного окна
        self.root.grid(row=0, column=0, sticky='nsew')

        self.scrollBar = tk.Scrollbar(self.root , orient='vertical') 
        self.canvas = tk.Canvas(self.root,width=750,height=600,bg='white') 
        self.canvas.configure(yscrollcommand=self.scrollBar.set)

        self.canvas.grid(row=0, column=0, sticky='nsew') # ,padx=[0, 4] чтобы увидеть замещённый root
        self.scrollBar.grid(row=0, column=1, sticky='ns')

        self.button_container = tk.Frame(self.canvas) # создаём контейнер для кнопок и помещаем его в canvas
        # настраиваем сетку для этого контейнера для корректного отображения кнопок методом grid
        for c in range(3): self.button_container.columnconfigure(index=c, weight=1)
        for r in range(100): self.button_container.rowconfigure(index=r, weight=1)

        self.add_buttons()

        self.canvas.create_window((0, 0), window=self.button_container,anchor='nw',width=750) 
        # Именно здесь очень важно указать размер окна чтобы ткинтер сам его не определял, ведь мы
        # с ним ещё будем работать при помощи сетки.


        self.button_container.bind("<Configure>", self.on_frame_configure)
        self.scrollBar.config(command=self.canvas.yview)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def pop_up_window(self,btn):
        self.process_btn(btn)

    def add_buttons(self):
        for y in range(100):
            for x in range(3):
                btn = tk.Button(self.button_container,text=f"",width=100,height=5)
                btn.config(command=lambda button=btn: self.pop_up_window(button)) 
                '''
                Создание лямбда-функции:
                lambda button=btn создает функцию с одним параметром button.
                btn передается как значение по умолчанию для этого параметра.
                Эта лямбда-функция назначается как команда для кнопки.
                Функция автоматически получает ссылку на саму кнопку благодаря параметру по умолчанию button=btn.
                '''

                btn.grid(row=y, column=x,padx=4,pady=4)