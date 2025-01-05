from tkinter import messagebox
'''
В Tkinter существуют два основных типа всплывающих окон:
MessageBox и Toplevel. 
MessageBox - маленькое всплывающее окно для уведомлений без функционала.
Toplevel - всплывающее окно которое можно настраивать: вставлять в него кнопки,
какие-то действия.
'''

var = messagebox.askquestion("Вопрос 1", "Вы сегодня хорошо поспали?")
print(var,type(var))
# далее будет проигрываться системный звук
print(messagebox.showinfo("Уведомление", "Вы успешно зарегестрировались!"))
print(messagebox.showerror("Ошибка", "Регистрация не удалась!"))

# тесты из коробки

if __name__ == "__main__":

    print("info", messagebox.showinfo("Spam", "Egg Information"))
    print("warning", messagebox.showwarning("Spam", "Egg Warning"))
    print("error", messagebox.showerror("Spam", "Egg Alert"))
    print("question", messagebox.askquestion("Spam", "Question?"))
    print("proceed", messagebox.askokcancel("Spam", "Proceed?"))
    print("yes/no", messagebox.askyesno("Spam", "Got it?"))
    print("yes/no/cancel", messagebox.askyesnocancel("Spam", "Want it?"))
    print("try again", messagebox.askretrycancel("Spam", "Try again?"))

#