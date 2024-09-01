import tkinter as tk
from tkinter import filedialog

class FileSavePage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.manager = self.master.manager

        self.dir_path = self.manager.getSavePath()

        self.header = tk.Label(self, text=f"Choose the result folder")
        self.header.pack(pady=(50, 0))

        self.pathLabel = tk.Label(self, text=f"Result folder: {self.dir_path}")
        self.pathLabel.pack(pady=5)

        self.saveBtn = tk.Button(self, text='Change the path to save', width=25, bg='white', highlightbackground='#383838', command=self.selectFolder)
        self.saveBtn.place(relx=0.5, rely=0.5, anchor='center')

        self.backBtn = tk.Button(self, text='Back', bg='white', highlightbackground='#262626', command=self.master.showOptionPage, width=15)
        self.backBtn.place(relx=0.3, rely=0.9, anchor='center')

        self.nextBtn = tk.Button(self, text='Next', bg='white', highlightbackground='#262626', command=self.nextPage, width=15)
        self.nextBtn.place(relx=0.7, rely=0.9, anchor='center')

    def selectFolder(self):
        _dir_path = filedialog.askdirectory(initialdir="/", title='Select the result folder')
        if _dir_path:
            self.dir_path = _dir_path
            self.pathLabel.configure(text=f"Result folder: {self.dir_path}")
            
    def nextPage(self):
        if self.dir_path:
            self.manager.setSavePath(self.dir_path + '/' + '.'.join(self.manager.getFilePath().split('/')[-1].split('.')[:-1]))
            self.master.showGeneratingPage()