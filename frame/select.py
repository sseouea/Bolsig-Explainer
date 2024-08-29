import tkinter as tk
from tkinter import filedialog
import os
import sys
from tkinter import font

class FileSelect(tk.Frame):
    def __init__(self, parent, command, txt, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.configure(background='#F2F2F2')
        self.master.label_.configure(bg='#A6A6A6')

        # var
        self.txt = txt
        self.command = command

        # label
        self.label1 = None
        self.label1 = tk.Label(self, text=f'Select the {self.txt} file', font=self.master.font, height=1, fg='black', bg='#F2F2F2')
        self.label1.grid(column=1)

        self.label2 = None
        self.label2 = tk.Label(self, text=f'{self.txt} file : ', font=self.master.font, height=1, fg='black', bg='#F2F2F2')
        self.label2.grid(column=1)
        
        # button
        self.button1 = None
        self.button1 = tk.Button(self, text='Upload', width=1, height=1, font=self.master.font, highlightbackground='#F2F2F2', fg='black', command=self.selectFile)
        self.button1.grid(column=1, ipadx=40, padx=10, pady=(100,0))

        self.button2 = None
        self.button2 = tk.Button(self, text='Next', width=1, height=1, font=self.master.font, highlightbackground='#F2F2F2', fg='black', command=self.optionSelect)
        self.button2.grid(column=1, ipadx=40, padx=10, pady=40)

        # file
        self.file = None
        
    def selectFile(self):
        _file = filedialog.askopenfile(
            initialdir=f'{os.getcwd()}',
            title=f'Select {self.txt} file (.txt .dat)',
            filetypes=(('txt files', '*.txt'), ('dat files', '*.dat'))
        )
        if _file:
            self.file = _file
            self.label2.configure(text=f'{self.txt} file: {self.file.name}')
            self.master.manager.setFilePath(self.file.name)
        
    def optionSelect(self):
        if self.file:
            if self.file.name.split('.')[-1] not in ['txt', 'dat']:
                self.command['error']()
                # self.master.showError()
            else:
                self.command['option']()
                # self.master.showOptionSelect()

    def getFilePath(self):
        if self.file:
            return self.file.name