import tkinter as tk
from tkinter import filedialog
import os
from DFmanager import *
import sys

class Finish(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text="All files be downloaded", fg='black')
        self.label.pack()

        self.button = tk.Button(self, text='Quit', width=15, height=3, borderwidth=1, background='white', fg='black', command=self.quit)
        self.button.pack()

    def quit(self):
        self.master.destroy()
        sys.exit()

class Generate(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.manager = manager
        self.label = tk.Label(self, text="Generating the file. Please wait a moment", fg='black')
        self.label.pack()

        self.manager.saveDF()
        self.after(2000, self.master.showFinish)

class FileSelect(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label1 = None
        self.label2 = None
        self.button1 = None
        self.button2 = None
        self.file = None

        self.label1 = tk.Label(self, text='Select the input file')
        self.label1.grid(row=1, column=0, padx=200, pady=30)

        self.button1 = tk.Button(self, text='Upload', font=12, command=self.selectFile)
        self.button1.grid(row=5, column=0, ipadx=40, padx=10, pady=20)

        self.label2 = tk.Label(self, text='', font=12, height=3)
        self.label2.grid(row=6, column=0, ipadx=40, padx=10, pady=20)

        self.button2 = tk.Button(self, text='Generate', font=12, command=self.generate)
        self.button2.grid(row=7, column=0, ipadx=40, padx=10, pady=20)

    def selectFile(self):
        self.file = filedialog.askopenfile(
            initialdir=f'{os.getcwd()}',
            title='Select input file (.csv)',
            filetypes=(('txt files', '*.txt'), ('dat files', '*.dat'))
        )
        self.label2.configure(text=f'Selected file: {self.file.name}')
        self.master.manager.setFilePath(self.file.name)

    def generate(self):
        if self.file:
            self.master.showGenerate()

class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Bolsig+ | Explainer")
        self.geometry('640x400+100+100')
        self.resizable(False, False)

        self.label = tk.Label(self, text="ver 1.0", fg='black')
        self.label.pack()

        self.button = tk.Button(self, text='Start', width=15, height=3, borderwidth=1, background='white', fg='black', command=self.showFileSelect)
        self.button.pack()

        self.manager = DFmanager()
        self.fileSelect = None
        self.generate = None

    def showFileSelect(self):
        self.label.pack_forget()
        self.button.pack_forget()
        self.fileSelect = FileSelect(self)
        self.fileSelect.pack(fill='both', expand=True)

    def showGenerate(self):
        if self.fileSelect:
            self.fileSelect.pack_forget()
        self.generate = Generate(self, self.manager)
        self.generate.pack(fill='both', expand=True)

    def showFinish(self):
        if self.generate:
            self.generate.pack_forget()
        self.finish = Finish(self)
        self.finish.pack(fill='both', expand=True)

if __name__ == "__main__":
    program = Program()
    program.mainloop()
