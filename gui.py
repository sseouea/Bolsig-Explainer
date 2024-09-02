import tkinter as tk
from manager.manager import *
from page.pages import *
import sys
from tkinter import font

class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initProgram()
        self.initLayout()
        self.showMainPage()
    
    def initProgram(self):
        self.fileLoadPage = None
        self.optionPage = None
        self.fileSavePage = None
        self.generatingPage = None
        self.resultPage = None
        self.errorPage = None

        self.manager = None
        self.fileType = None
        self.options = {}

    def initLayout(self):
        self.title("Bolsig+ | Explainer")

        self.geometry('800x500+100+100')
        self.resizable(False, False)

        self.font = font.Font(family="Helvetica", size=12)
        self.option_add("*Font", self.font)

        # self.bg = '#F5F5F5'
        # self.configure(background=self.bg)

        self.header = tk.Label(self, text='Bolsig+ | Explainer')
        self.header.place(relx=0.5, rely=0.2, anchor='center')

        self.footer = tk.Label(self, text="ver 1.6 | sseouea03@gmail.com", fg='white', bg='#262626', anchor='e', padx=15)
        self.footer.pack(side='bottom', fill='x')

    def clean(self):
        if self.fileLoadPage:
            self.fileLoadPage.pack_forget()
        if self.optionPage:
            self.optionPage.pack_forget()
        if self.fileSavePage:
            self.fileSavePage.pack_forget()
        if self.generatingPage:
            self.generatingPage.pack_forget()
        if self.errorPage:
            self.errorPage.pack_forget()
        if self.resultPage:
            self.resultPage.pack_forget()
        
    def showMainPage(self):
        self.clean()

        self.inputBtn = tk.Button(self, text='Select Input File', bg='white', width=20, command=self.showInputFileLoadPage)
        self.inputBtn.pack(pady=(200, 10))

        self.outputBtn = tk.Button(self, text='Select Output File', bg='white', width=20, command=self.showOutputFileLoadPage)
        self.outputBtn.pack(pady=10)

        self.exitBtn = tk.Button(self, text='Exit', bg='white', width=20, command=self.exitProgram)
        self.exitBtn.pack(pady=10)

    def showInputFileLoadPage(self):
        self.manager = iManager()
        self.fileType = 'input'
        self.showFileLoadPage()

    def showOutputFileLoadPage(self):
        self.manager = oManager()
        self.fileType = 'output'
        self.showFileLoadPage()
    
    def showFileLoadPage(self):
        self.clean()
        self.header.pack_forget()
        self.inputBtn.pack_forget()
        self.outputBtn.pack_forget()
        self.exitBtn.pack_forget()

        try:
            self.fileLoadPage = FileLoadPage(self)
            self.fileLoadPage.pack(fill='both', expand=True)
        except Exception as e:
            self.showErrorPage(e, self.showFileLoadPage)

    def showOptionPage(self):
        self.clean()
        try:
            self.optionPage = OptionPage(self)
            self.optionPage.pack(fill='both', expand=True)
        except Exception as e:
            self.showErrorPage(e, self.showOptionPage)

    def showFileSavePage(self):
        self.clean()
        try:
            self.fileSavePage = FileSavePage(self)
            self.fileSavePage.pack(fill='both', expand=True)
        except Exception as e:
            self.showErrorPage(e, self.showFileSavePage)

    def showGeneratingPage(self):
        self.clean()
        try:
            self.generatingPage = GeneratingPage(self)
            self.generatingPage.pack(fill='both', expand=True)
        except Exception as e:
            self.showErrorPage(e, self.showFileSavePage)

    def showResultPage(self):
        self.clean()
        try:
            self.resultPage = ResultPage(self)
            self.resultPage.pack(fill='both', expand=True)
        except Exception as e:
            self.showErrorPage(e, self.showResultPage)

    def showErrorPage(self, errorMsg, showPrevPage):
        self.clean()
        self.errorPage = ErrorPage(self, errorMsg, showPrevPage)
        self.errorPage.pack(fill='both', expand=True)
    
    def exitProgram(self):
        self.destroy()
        sys.exit()
