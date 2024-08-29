import tkinter as tk
import os
import sys
from tkinter import font

class OptionSelect(tk.Frame):
    def __init__(self, parent, manager, type, command, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # var
        self.type = type
        self.command = command

        self.master.options[self.type] = list()
        self.master.label_.configure(bg='#A6A6A6')
        self.configure(background='#F2F2F2')

        # manager
        self.manager = manager

        if type == 'input':
            self.manager.setOptionAndCountDF()

            self.df = self.manager.getCountDF()
            if self.df.empty:
                raise Exception('EmptyDataFrameError')
            else:
                self.df = self.df.rename(columns={'option' : 'key', 'count' : 'value'})
            
        elif type == 'output':
            pass ###
        
        # label
        self.label = tk.Label(self, text="Choose the option (default = 'All species/types')", height=1, font=self.master.font, fg='black', bg='#F2F2F2')
        self.label.pack()
        self.label_ = tk.Label(self, text="options :", height=1, font=self.master.font, fg='black', bg='#F2F2F2')
        self.label_.pack()

        # scroll
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

        # button
        self.buttons = list()
        
        for index, row in self.df.iterrows():
            button = tk.Button(self.scrollable_frame, text=f"{row['key']} ({row['value']})",
                               font=self.master.font, highlightbackground='#F2F2F2', fg='black', width=10, height=1,
                               command=lambda idx=index: self.on_button_click(idx+1))
            if index == 0:
                button.pack(fill="x", padx=5, pady=(20,5))
            elif index == len(self.df)-1:
                button.pack(fill="x", padx=5, pady=(5,20))
            else:
                button.pack(fill="x", padx=5, pady=5)
            self.buttons.append(button)

        self.select_button = tk.Button(self, text="Select", width=15, height=1, font=self.master.font, highlightbackground='#F2F2F2', fg='black', command=self.name)
        self.select_button.pack(expand=True, padx=5, pady=(40,60))

    def on_button_click(self, idx):
        button = self.buttons[idx-1]
        if idx in self.master.options[self.type]:
            self.master.options[self.type].remove(idx)
            button.configure(highlightbackground='#F2F2F2', fg='black')
        else:
            self.master.options[self.type].append(idx)
            button.configure(highlightbackground='#F2F2F2', fg='light gray')
            
        button.pack(fill="x", pady=5)
        self.master.options[self.type].sort()
        text = list(map(lambda idx : self.df.loc[idx-1, 'key'], self.master.options[self.type]))
        text = ', '.join(text)
        self.label_.configure(text=f"options : {text}")
        self.label_.pack()

    def name(self):
        if len(self.master.options) == 0:
            self.master.options = None

        if self.type == 'input':
            self.manager.setChoosedDF(self.master.options)
        else:
            pass ###

        self.command() # self.master.showName()