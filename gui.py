import tkinter as tk
from tkinter import filedialog
import os
from DFmanager import *
import sys

class Finish(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg='#262626')
        self.master.label_.configure(bg='#262626')
        self.pack(fill="both", expand=True)
        self.label = tk.Label(self, text="All files be downloaded", height=1, font=12, fg='white', bg='#262626')
        self.label.pack()

        self.button_frame = tk.Frame(self, bg='#262626')
        self.button_frame.pack(expand=True)

        button_width = 5

        self.button1 = tk.Button(self.button_frame, text='Select', height=1, font=12, fg='black', highlightbackground='#262626', width=button_width, command=self.master.showFileSelect)
        self.button1.pack(side=tk.LEFT, expand=True, fill="both", padx=10)

        self.button2 = tk.Button(self.button_frame, text='Quit', height=1, font=12, fg='black', highlightbackground='#262626', width=button_width, command=self.quit)
        self.button2.pack(side=tk.RIGHT, expand=True, fill="both", padx=10)

    def quit(self):
        self.master.destroy()
        sys.exit()

class Generate(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.manager = manager
        self.configure(bg='#383838')
        self.master.label_.configure(bg='#262626')
        self.label = tk.Label(self, text="Generating the file\n Please wait a moment", height=2, font=12, fg='white', bg='#383838')
        self.label.pack()

        self.manager.saveDF()
        self.after(2000, self.master.showFinish)

class Name(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg='#383838')
        self.manager = manager
        self.master.label_.configure(bg='#262626')
        self.dir_path = self.manager.getSavePath()
        self.pack(fill="both", expand=True)

        self.label = tk.Label(self, text=f"Choose output folder", height=1, font=12, fg='white', bg='#383838')
        self.label.pack()
        self.label_ = tk.Label(self, text=f"output folder : {self.dir_path}", height=1, font=12, fg='white', bg='#383838')
        self.label_.pack()

        self.button = tk.Button(self, text='Choose', height=1, width=7, font=12, fg='black', highlightbackground='#383838', comman=self.choose)
        self.button.pack(expand=True)

        self.button1 = tk.Button(self, text='Enter', height=1, width=7, font=12, fg='black', highlightbackground='#383838', comman=self.enter)
        self.button1.pack(expand=True)

        self.button2 = tk.Button(self, text='Option', height=1, width=7, font=12, fg='black', highlightbackground='#383838', command=self.master.showOptionSelect)
        self.button2.pack(expand=True)

        self.button3 = tk.Button(self, text='Select', height=1, width=7, font=12, fg='black', highlightbackground='#383838', command=self.master.showFileSelect)
        self.button3.pack(expand=True)

    def choose(self):
        _dir_path = filedialog.askdirectory(initialdir="/", title='Select the output folder')
        if _dir_path:
            self.dir_path = _dir_path
            self.label_.configure(text=f"output folder : {self.dir_path}")
            
    def enter(self):
        if self.dir_path:
            self.manager.setSavePath(self.dir_path + '/' + '.'.join(self.manager.getFilePath().split('/')[-1].split('.')[:-1]))
            self.master.showGenerate()

class Error(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg='#383838')
        self.master.label_.configure(bg='#262626')
        self.pack(fill="both", expand=True)

        self.label = tk.Label(self, text=f"Input file format is dismatched (extension, data etc.)\n\nfile path : {self.master.fileSelect.getFilePath()}", height=3, font=12, fg='white', bg='#383838')
        self.label.pack(side=tk.TOP, pady=(10, 20))

        self.button_frame = tk.Frame(self, bg='#383838')
        self.button_frame.pack(expand=True)

        button_width = 5

        self.button1 = tk.Button(self.button_frame, text='Select', height=1, font=12, fg='black', highlightbackground='#383838', width=button_width, command=self.master.showFileSelect)
        self.button1.pack(side=tk.LEFT, expand=True, fill="both", padx=10)

        self.button2 = tk.Button(self.button_frame, text='Quit', height=1, font=12, fg='black', highlightbackground='#383838', width=button_width, command=self.quit)
        self.button2.pack(side=tk.RIGHT, expand=True, fill="both", padx=10)

    def quit(self):
        self.master.destroy()
        sys.exit()

class OptionSelect(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.manager = manager
        self.manager.setOptionAndCountDF()
        self.master.options = list()
        self.master.label_.configure(bg='#A6A6A6')
        self.configure(background='#F2F2F2')

        self.label = tk.Label(self, text="Choose the option (default = 'All species')", height=1, font=12, fg='black', bg='#F2F2F2')
        self.label.pack()
        self.label_ = tk.Label(self, text="options :", height=1, font=12, fg='black', bg='#F2F2F2')
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
        self.canvas.configure(yscrollcommand=self.scrollbar.set, bg='#F2F2F2', bd=0, highlightthickness=0)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollable_frame.configure(background='#F2F2F2')
        self.scrollbar.pack(side="right", fill="y")

        self.df = self.manager.getCountDF()
        self.buttons = list()

        if self.df.empty:
            raise Error
        
        for index, row in self.df.iterrows():
            button = tk.Button(self.scrollable_frame, text=f"{row['option']} ({row['count']})",
                               font=12, highlightbackground='#F2F2F2', fg='black', width=10, height=1,
                               command=lambda idx=index: self.on_button_click(idx+1))
            button.pack(fill="x", padx=5, pady=5)
            self.buttons.append(button)

        self.select_button = tk.Button(self, text="Select", width=15, height=1, font=12, highlightbackground='#F2F2F2', fg='black', command=self.name)
        self.select_button.pack(expand=True, padx=5, pady=20)

    def on_button_click(self, idx):
        button = self.buttons[idx-1]
        if idx in self.master.options:
            self.master.options.remove(idx)
            button.configure(highlightbackground='#F2F2F2', fg='black')
        else:
            self.master.options.append(idx)
            button.configure(highlightbackground='#F2F2F2', fg='light gray')
            
        button.pack(fill="x", pady=5)
        self.master.options.sort()
        text = list(map(lambda idx : self.df.loc[idx-1, 'option'], self.master.options))
        text = ', '.join(text)
        self.label_.configure(text=f"options : {text}")
        self.label_.pack()

    def name(self):
        if len(self.master.options) == 0:
            self.master.options = None
        self.manager.setChoosedDF(self.master.options)
        self.master.showName()

class FileSelect(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label1 = None
        self.label2 = None
        self.button1 = None
        self.button2 = None
        self.file = None
        self.master.label_.configure(bg='#A6A6A6')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='#F2F2F2')
        self.label1 = tk.Label(self, text='Select the input file', font=12, height=1, fg='black', bg='#F2F2F2')
        self.label1.grid(row=1, column=1, padx=200, pady=30)

        self.button1 = tk.Button(self, text='Upload', width=1, height=1, font=12, highlightbackground='#F2F2F2', fg='black', command=self.selectFile)
        self.button1.grid(row=5, column=1, ipadx=40, padx=10, pady=20)

        self.label2 = tk.Label(self, text='', font=12, height=1, fg='black', bg='#F2F2F2')
        self.label2.grid(row=6, column=1, ipadx=40, padx=10, pady=20)

        self.button2 = tk.Button(self, text='Next', width=1, height=1, font=12, highlightbackground='#F2F2F2', fg='black', command=self.optionSelect)
        self.button2.grid(row=7, column=1, ipadx=40, padx=10, pady=20)

    def selectFile(self):
        self.file = filedialog.askopenfile(
            initialdir=f'{os.getcwd()}',
            title='Select input file (.txt .dat)',
            filetypes=(('txt files', '*.txt'), ('dat files', '*.dat'))
        )
        if self.file:
            self.label2.configure(text=f'Selected file: {self.file.name}')
            self.master.manager.setFilePath(self.file.name)
        
    def optionSelect(self):
        if self.file:
            if self.file.name.split('.')[-1] not in ['txt', 'dat']:
                self.master.showError()
            else: self.master.showOptionSelect()

    def getFilePath(self):
        if self.file:
            return self.file.name

class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Bolsig+ | Explainer")
        self.geometry('640x400+100+100')
        self.resizable(False, False)
        self.configure(background='#262626')

        self.label = tk.Label(self, text="ver 1.5", height=1, font=12, fg='white', background='#262626')
        self.label.pack(side=tk.TOP, fill=tk.X)

        self.label_ = tk.Label(self, text="sseouea03@gmail.com", height=1, font=12, fg='white', background='#262626', compound='bottom')
        self.label_.pack(side=tk.BOTTOM, fill=tk.X)

        self.button = tk.Button(self, text='Start', background='white', width=5, height=1, font=12, fg='black', highlightbackground='#262626', command=self.showFileSelect)
        self.button.pack(expand=True, pady=5)

        self.manager = DFmanager()
        self.fileSelect = None
        self.options = list()
        self.optionSelect = None
        self.generate = None
        self.error = None
        self.finish = None
        self.name = None

    def clean(self):
        if self.fileSelect:
            self.fileSelect.pack_forget()
        if self.optionSelect:
            self.optionSelect.pack_forget()
        if self.generate:
            self.generate.pack_forget()
        if self.error:
            self.error.pack_forget()
        if self.finish:
            self.finish.pack_forget()
        if self.name:
            self.name.pack_forget()

    def showFileSelect(self):
        self.clean()
        self.label.pack_forget()
        self.button.pack_forget()
        self.fileSelect = FileSelect(self)
        self.fileSelect.pack(fill='both', expand=True)

    def showOptionSelect(self):
        self.clean()

        try:
            self.optionSelect = OptionSelect(self, self.manager)
            self.optionSelect.pack(fill='both', expand=True)
        except:
            self.showError()

    def showName(self):
        self.clean()
        self.name = Name(self, self.manager)
        self.name.pack(fill='both', expand=True)

    def showGenerate(self):
        self.clean()
        self.generate = Generate(self, self.manager)
        self.generate.pack(fill='both', expand=True)

    def showFinish(self):
        self.clean()
        self.finish = Finish(self)
        self.finish.pack(fill='both', expand=True)

    def showError(self):
        self.clean()
        self.error = Error(self)
        self.error.pack(fill='both', expand=True)
