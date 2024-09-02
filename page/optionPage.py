import tkinter as tk
import pandas as pd

class OptionPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # var
        self.fileType = self.master.fileType
        self.master.options[self.fileType] = list()
        self.manager = self.master.manager

        # manager
        if self.fileType == 'input':
            self.manager.setOptionAndCountDF()

            self.df = self.manager.getCountDF()
            if self.df.empty:
                raise Exception('EmptyDataFrameError')
            else:
                self.df = self.df.rename(columns={'option' : 'key', 'count' : 'value'})
            
        elif self.fileType == 'output':
            self.df = pd.DataFrame({'key' : ['Input cross section', 'Conditions', 'Rate coefficients (m3/s)', 'Energy loss coefficients (eV m3/s)', 'Inverse rate coefficients (m3/s)', 'Transport coefficients'], 'value' : [None]*6})
            self.manager.setProcessedDF()
            for key in self.manager.processedDF:
                if type(self.manager.processedDF[key]) == type(None):
                    self.df[key] = False
                else:
                    self.df[key] = True
        

        # label
        self.header = tk.Label(self, text="Choose the options (default = 'All species/types')")
        self.header.pack(pady=(50,0))

        self.optionLabel = tk.Label(self, text='Options: All')
        self.optionLabel.pack(pady=5)

        # scroll
        # self.scrollbar = tk.Scrollbr(self.canvas, orient="vertical", command=self.canvas.yview)
        self.innerFrame = tk.Frame(self)

        self.canvas = tk.Canvas(self.innerFrame)

        self.scrollFrame= tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar(self.innerFrame, command=self.canvas.yview)

        self.windowId = self.canvas.create_window((0, 0), window=self.scrollFrame, anchor='nw')

        def _configScrollFrame(event):
            size = (self.scrollFrame.winfo_reqwidth(), self.scrollFrame.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)
            if self.scrollFrame.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=self.scrollFrame.winfo_reqwidth())
        self.scrollFrame.bind('<Configure>', _configScrollFrame)

        self.canvas.yview_moveto(0)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill='both', expand=True)

        self.innerFrame.place(relx=0.5, rely=0.55, anchor='center')

        # button
        self.btnList = list()

        if self.fileType == 'input':
            self.btnWidth = 15
            self.colCnt = 3
        else:
            self.btnWidth = 35
            self.colCnt = 1
            
        
        for index, row in self.df.iterrows():
            if self.fileType == 'input':
                btn = tk.Button(self.scrollFrame, text=f"{row['key']} ({row['value']})",
                                width=self.btnWidth,
                                command=lambda idx=index: self.on_button_click(idx+1))
            elif self.fileType == 'output':
                if row[row['key']]:
                    btn = tk.Button(self.scrollFrame, text=f"{row['key']}",
                                width=self.btnWidth,
                                command=lambda idx=index: self.on_button_click(idx+1))
                else:
                    btn = tk.Button(self.scrollFrame, text=f"{row['key']}",
                                width=self.btnWidth, bg='#555', disabledforeground='light gray', state='disabled',
                                command=lambda idx=index: self.on_button_click(idx+1))
            btn.grid(row=index//self.colCnt, column=index%self.colCnt, padx=5, pady=5)
            self.btnList.append(btn)

        self.backBtn = tk.Button(self, text='Back', bg='white', command=self.master.showFileLoadPage, width=15)
        self.backBtn.place(relx=0.3, rely=0.9, anchor='center')

        self.nextBtn = tk.Button(self, text='Next', bg='white', command=self.nextPage, width=15)
        self.nextBtn.place(relx=0.7, rely=0.9, anchor='center')

    def on_button_click(self, idx):
        button = self.btnList[idx-1]
        if idx in self.master.options[self.fileType]:
            self.master.options[self.fileType].remove(idx)
            button.configure(bg='#F2F2F2', fg='black')
        else:
            self.master.options[self.fileType].append(idx)
            button.configure(bg='#AAA', fg='light gray')
            
        button.grid(row=(idx-1)//self.colCnt, column=(idx-1)%self.colCnt, padx=5, pady=5)
        self.master.options[self.fileType].sort()
        text = list(map(lambda idx : self.df.loc[idx-1, 'key'], self.master.options[self.fileType]))
        text = ', '.join(text)

        if text == '':
            text = 'All'
        self.optionLabel.configure(text=f"options: {text}")
        self.optionLabel.pack()

    def nextPage(self):
        if len(self.master.options[self.fileType]) == 0:
            if self.fileType == 'input':
                self.master.options[self.fileType] = None
            elif self.fileType == 'output':
                self.master.options[self.fileType] = ['all']
        else:
            if self.fileType == 'output':
                self.master.options[self.fileType] = list(map(lambda idx : self.df['key'].iloc[idx-1], self.master.options[self.fileType]))

        if self.fileType == 'input':
            self.manager.setChoosedDF(self.master.options[self.fileType])
        else:
            pass

        self.master.showFileSavePage()