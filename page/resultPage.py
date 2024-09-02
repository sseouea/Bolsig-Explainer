import tkinter as tk
import sys

class ResultPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.header = tk.Label(self, text="All files are downloaded")
        self.header.pack(pady=(50, 0))

        self.restartBtn = tk.Button(self, text='Return to main', bg='white', command=self.master.showMainPage, width=15)
        self.restartBtn.place(relx=0.3, rely=0.6, anchor='center')

        self.exitBtn = tk.Button(self, text='Exit', bg='white', command=self.master.exitProgram, width=15)
        self.exitBtn.place(relx=0.7, rely=0.6, anchor='center')