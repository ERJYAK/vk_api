import tkinter
from API import ARI

class MainWindow:
    def __init__(self, width=300, heihgt=400):
        self.root = tkinter.Tk()
        self.root.geometry('{}x{}'.format(width, heihgt))
        self.exit_btn = tkinter.Button(self.root, text='Выход', command=self.exit)
        self.start_btn = tkinter.Button(self.root, text='Включить', command=self.start)
        self.pause_btn = tkinter.Button(self.root, text="Пауза", command=self.pause)

    def draw_widgets(self):
        self.start_btn.pack()
        self.pause_btn.pack()
        self.exit_btn.pack()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def start(self):
        session = ARI()
        session.run()

    def pause(self):
        pass

    def exit(self):
        self.root.destroy()