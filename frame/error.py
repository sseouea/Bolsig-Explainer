import tkinter as tk
import os
import sys
from tkinter import font

class Error(tk.Frame):
    def __init__(self, parent, txt, command, frame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.configure(bg='#383838')
        self.master.label_.configure(bg='#262626')
        self.pack(fill="both", expand=True)

        # var
        self.txt = txt
        self.frame = frame
        self.filePath = frame.getFilePath() # self.master.fileSelect.getFilePath()

        # label
        self.label = tk.Label(self, text=f"{self.txt} file format is dismatched (extension, data etc.)\nfile path : {self.filePath}", height=3, font=self.master.font, fg='white', bg='#383838')
        self.label.pack(side=tk.TOP)

        # button
        button_width = 5
        self.button_frame = tk.Frame(self, bg='#383838')
        self.button_frame.pack(expand=True)

        self.button1 = tk.Button(self.button_frame, text='Select', height=1, font=self.master.font, fg='black', highlightbackground='#383838', width=button_width, command=command) # self.master.showFileSelect
        self.button1.pack(side=tk.LEFT, expand=True, fill="both", padx=10, pady=(40,60))

        self.button2 = tk.Button(self.button_frame, text='Quit', height=1, font=self.master.font, fg='black', highlightbackground='#383838', width=button_width, command=self.quit)
        self.button2.pack(side=tk.RIGHT, expand=True, fill="both", padx=10, pady=(40,60))

    def setFilePath(self):        
        self.filepath = self.frame.getFilePath()
        self.label = tk.Label(self, text=f"{self.txt} file format is dismatched (extension, data etc.)\nfile path : {self.filePath}", height=3, font=self.master.font, fg='white', bg='#383838')
        self.label.pack(side=tk.TOP)

    def quit(self):
        self.master.destroy()
        sys.exit()