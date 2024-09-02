import tkinter as tk
from tkinter import filedialog
import os

class FileLoadPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # var
        self.fileType = self.master.fileType
        self.file = None

        # label
        self.header = tk.Label(self, text=f'Select the {self.fileType} file')
        self.header.pack(pady=(50,0))

        self.pathLabel = tk.Label(self, text='File path: None')
        self.pathLabel.pack(pady=5)
        
        # button
        self.loadBtn = tk.Button(self, text=f'Load {self.fileType} file', bg='white', command=self.selectFile, width=20)
        self.loadBtn.place(relx=0.5, rely=0.5, anchor='center')

        self.backBtn = tk.Button(self, text='Back', bg='white', command=self.master.showMainPage, width=15)
        self.backBtn.place(relx=0.3, rely=0.9, anchor='center')

        self.nextBtn = tk.Button(self, text='Next', bg='white', command=self.nextPage, width=15)
        self.nextBtn.place(relx=0.7, rely=0.9, anchor='center')

        
    def selectFile(self):
        _file = filedialog.askopenfile(
            initialdir=f'{os.getcwd()}',
            title=f'Select {self.fileType} file (.txt .dat)',
            filetypes=(('txt files', '*.txt'), ('dat files', '*.dat'))
        )
        if _file:
            self.file = _file
            self.pathLabel.configure(text=f'File path: {self.file.name}')
    
    def nextPage(self):
            if self.file == None:
                self.master.showErrorPage("No file selected", self.master.showFileLoadPage)
            elif self.file.name.split('.')[-1] not in ['txt', 'dat']:
                self.master.showErrorPage("The file extension must be 'txt' or 'dat'", self.master.showFileLoadPage)
            else:
                self.master.manager.setFilePath(self.file.name)
                self.master.showOptionPage()