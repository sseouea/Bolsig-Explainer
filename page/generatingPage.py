import tkinter as tk

class GeneratingPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.manager = self.master.manager
        self.fileType = self.master.fileType 
        
        self.configure(bg='#383838')

        self.label = tk.Label(self, text="Generating the files\n Please wait a moment", fg='white', bg='#383838')
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        if self.fileType == 'input':
            self.manager.saveDF()
        elif self.fileType == 'output':
            for option in self.master.options[self.fileType]:
                self.manager.saveDF(option)
                
        self.after(1000, self.master.showResultPage)
