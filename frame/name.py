import tkinter as tk
import os
import sys
from tkinter import font

class Name(tk.Frame):
    def __init__(self, parent, manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg='#383838')
        self.manager = manager
        self.master.label_.configure(bg='#262626')
        self.dir_path = self.manager.getSavePath()
        self.pack(fill="both", expand=True)

        self.label = tk.Label(self, text=f"Choose output folder", height=1, font=self.master.font, fg='white', bg='#383838')
        self.label.pack()
        self.label_ = tk.Label(self, text=f"output folder : {self.dir_path}", height=1, font=self.master.font, fg='white', bg='#383838')
        self.label_.pack()

        self.button = tk.Button(self, text='Choose', height=1, width=7, font=self.master.font, fg='black', highlightbackground='#383838', comman=self.choose)
        self.button.pack(expand=True, pady=(40,5))

        self.button1 = tk.Button(self, text='Enter', height=1, width=7, font=self.master.font, fg='black', highlightbackground='#383838', comman=self.enter)
        self.button1.pack(expand=True, pady=(5,5))

        self.button2 = tk.Button(self, text='Option', height=1, width=7, font=self.master.font, fg='black', highlightbackground='#383838', command=self.master.showOptionSelect)
        self.button2.pack(expand=True, pady=(5,5))

        self.button3 = tk.Button(self, text='Select', height=1, width=7, font=self.master.font, fg='black', highlightbackground='#383838', command=self.master.showFileSelect)
        self.button3.pack(expand=True, pady=(5,40))

    def choose(self):
        _dir_path = filedialog.askdirectory(initialdir="/", title='Select the output folder')
        if _dir_path:
            self.dir_path = _dir_path
            self.label_.configure(text=f"output folder : {self.dir_path}")
            
    def enter(self):
        if self.dir_path:
            self.manager.setSavePath(self.dir_path + '/' + '.'.join(self.manager.getFilePath().split('/')[-1].split('.')[:-1]))
            self.master.showGenerate()