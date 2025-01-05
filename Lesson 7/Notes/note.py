import tkinter as tk
from tkinter import messagebox

class Note:
    def __init__(self,name,text):
        self._name = name
        self._text = text

    def get_name(self):
        return self._name
    
    def get_text(self):
        return self._text

    # def change_name(self,new_name):
    #     self._name = new_name

    # def change_text(self,new_text):
    #     self._text = new_text
        
class Create_note:

    def __init__(self,notes):
        self.notes = notes

    def start(self,btn):
        self.btn = btn

        # self.root=tk.Toplevel()
        # self.root.title("Создание заметки")
        # self.root.geometry("300x100")
        # self.root.resizable(False, False) # запрещаем растягивать

        self.meeting_window()

    def meeting_window(self):

        action = messagebox.askquestion("Уведомление", "Желаете создать заметку?")
        if action == 'yes':
            self.process_btn_yes()
        '''
        Этот код был сделан до того как я открыл для себя messagebox :)

        # label = tk.Label(self.root, text="Желаете создать заметку?")
        # label.place(relx=0.5, rely=0.2,anchor="c")

        # btnYes = tk.Button(self.root, text="Да",width=3, height=2, command=self.process_btn_yes)
        # btnNo  = tk.Button(self.root, text="Нет",width=3,height=2, command=self.root.destroy)

        # btnYes.place(relx=0.4, rely=0.6,anchor="c")
        # btnNo.place(relx=0.6, rely=0.6,anchor="c")
        '''

    def process_btn_yes(self):


        self.root=tk.Toplevel()
        self.root.title("Создание заметки")
        self.root.geometry("300x100")
        self.root.resizable(False, False) # запрещаем растягивать

        label_name = tk.Label (self.root,text = 'Имя')
        label_name.place(x=0,y=0)
        name_note = tk.Text(self.root,width=15,height=1)
        name_note.place(x=40,y=0)

        label_text = tk.Label(self.root,text = 'Текст')
        label_text.place(x=0,y=30)
        text_note = tk.Text(self.root,width=30,height=3)
        text_note.place(x=40,y=30)


        create_note = tk.Button(self.root,text = 'Создать заметку',width=15,height=1, \
                                command=lambda: self.save_note(name_note.get(1.0,tk.END),text_note.get(1.0,tk.END)))
        create_note.place(x=170,y=0)


    def save_note(self,name,text):
        self.notes[self.btn]=Note(name,text)
        self.btn.configure(text = name)
        self.root.destroy()


class Show_note:
    def __init__(self,current_note):
        messagebox.showinfo("Содержание", current_note.get_text())


        # self.title(f"Содержание заметки")
        # self.geometry("300x100")
        # tk.Label(self,text=current_note.get_text()).pack()


