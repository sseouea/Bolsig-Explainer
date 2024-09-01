import tkinter as tk

class ErrorPage(tk.Frame):
    def __init__(self, parent, errorMsg, showPrevPage, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.configure(bg='#383838')

        # label
        self.errorLabel = tk.Label(self, text=f"Error: {errorMsg}", fg='white', bg='#383838')
        self.errorLabel.place(relx=0.5, rely=0.4, anchor='center')

        # button
        self.backBtn = tk.Button(self, text='Back', bg='white', highlightbackground='#262626', command=showPrevPage, width=15)
        self.backBtn.place(relx=0.3, rely=0.6, anchor='center')

        self.exitBtn = tk.Button(self, text='Exit', bg='white', highlightbackground='#262626', command=self.master.exitProgram, width=15)
        self.exitBtn.place(relx=0.7, rely=0.6, anchor='center')