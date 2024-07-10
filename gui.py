import tkinter as tk
from tkinter import filedialog
import os
from DFmanager import *
import sys

class Finish(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text="All files be downloaded", fg='white')
        self.label.pack()

        self.button = tk.Button(self, text='Quit', background='white', fg='black', command=self.quit)
        self.button.pack(expand=True)

    def quit(self):
        self.master.destroy()
        sys.exit()

class Generate(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.manager = manager
        self.label = tk.Label(self, text="Generating the file. Please wait a moment", fg='white')
        self.label.pack()

        self.manager.saveDF()
        self.after(2000, self.master.showFinish)

class OptionSelect(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.manager = manager
        self.manager.setOptionAndCountDF()
        self.label = tk.Label(self, text="Choose the option", fg='white')
        self.label.pack()
        self.label_ = tk.Label(self, text="options :", fg='white')
        self.label_.pack()

        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.df = self.manager.getCountDF()
        self.buttons = list()
        for index, row in self.df.iterrows():
            button = tk.Button(self.scrollable_frame, text=f"{row['option']} ({row['count']})",
                               font=12, background='white', fg='black',
                               command=lambda idx=index: self.on_button_click(idx+1))
            button.pack(fill="x", pady=5)
            self.buttons.append(button)

        self.select_button = tk.Button(self, text="Select (or 'All species')", font=12, background='white', fg='black', command=self.generate)
        self.select_button.pack(expand=True, pady=20)

    def on_button_click(self, idx):
        button = self.buttons[idx-1]
        if idx in self.master.options:
            self.master.options.remove(idx)
            button.configure(background='white', fg='black')
        else:
            self.master.options.append(idx)
            button.configure(background='white', fg='light grey')
            
        button.pack(fill="x", pady=5)
        self.master.options.sort()
        text = list(map(lambda idx : self.df.loc[idx-1, 'option'], self.master.options))
        text = ', '.join(text)
        self.label_.configure(text=f"options : {text}")
        self.label_.pack()

    def generate(self):
        if len(self.master.options) == 0:
            self.master.options = None
        self.manager.setChoosedDF(self.master.options)
        self.master.showGenerate()

class FileSelect(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label1 = None
        self.label2 = None
        self.button1 = None
        self.button2 = None
        self.file = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.label1 = tk.Label(self, text='Select the input file', fg='white')
        self.label1.grid(row=1, column=1, padx=200, pady=30)

        self.button1 = tk.Button(self, text='Upload', font=12, background='white', fg='black', command=self.selectFile)
        self.button1.grid(row=5, column=1, ipadx=40, padx=10, pady=20)

        self.label2 = tk.Label(self, text='', font=12, height=3, fg='white')
        self.label2.grid(row=6, column=1, ipadx=40, padx=10, pady=20)

        self.button2 = tk.Button(self, text='Next', font=12, background='white', fg='black', command=self.optionSelect)
        self.button2.grid(row=7, column=1, ipadx=40, padx=10, pady=20)

    def selectFile(self):
        self.file = filedialog.askopenfile(
            initialdir=f'{os.getcwd()}',
            title='Select input file (.txt .dat)',
            filetypes=(('txt files', '*.txt'), ('dat files', '*.dat'))
        )
        self.label2.configure(text=f'Selected file: {self.file.name}')
        self.master.manager.setFilePath(self.file.name)

    def optionSelect(self):
        if self.file:
            self.master.showOptionSelect()

class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Bolsig+ | Explainer")
        self.geometry('640x400+100+100')
        self.resizable(False, False)

        self.label = tk.Label(self, text="ver 1.0", fg='white')
        self.label.pack(side=tk.TOP, fill=tk.X)

        self.label_ = tk.Label(self, text="sseouea03@gmail.com", fg='white', compound='bottom')
        self.label_.pack(side=tk.BOTTOM, fill=tk.X)

        self.button = tk.Button(self, text='Start', background='white', fg='black', command=self.showFileSelect)
        self.button.pack(expand=True)

        self.manager = DFmanager()
        self.fileSelect = None
        self.options = list()
        self.optionSelect = None
        self.generate = None

    def showFileSelect(self):
        self.label.pack_forget()
        self.button.pack_forget()
        self.fileSelect = FileSelect(self)
        self.fileSelect.pack(fill='both', expand=True)

    def showOptionSelect(self):
        if self.fileSelect:
            self.fileSelect.pack_forget()
        self.optionSelect = OptionSelect(self, self.manager)
        self.optionSelect.pack(fill='both', expand=True)

    def showGenerate(self):
        if self.optionSelect:
            self.optionSelect.pack_forget()
        self.generate = Generate(self, self.manager)
        self.generate.pack(fill='both', expand=True)

    def showFinish(self):
        if self.generate:
            self.generate.pack_forget()
        self.finish = Finish(self)
        self.finish.pack(fill='both', expand=True)
