from note import Create_note
from note import Show_note
from main_window import mainWindow

class Main:
    def __init__(self):
        self.view = mainWindow(self.process_button)
        self.notes = {}
        self.creating = Create_note(self.notes)

    def process_button(self,btn):
        if btn in self.notes:
            Show_note(self.notes[btn])
        else:
            self.creating.start(btn)
    
    def start(self):
        self.view.mainloop()

if __name__ == '__main__':
    Main().start()

    