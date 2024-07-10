import os
from pathlib import Path
import pandas as pd
from functions import *

class DFmanager:
    def __init__(self):
        self.filePath = None
        self.savePath = None
        self.originDF = None
        self.countDF = None
        self.optionDF = None
        self.choosedDF = None

    def setFilePath(self, path):
        if not os.path.exists(path):
            return 'No file'
        
        ext = path.split('.')[-1]
        _path = '.'.join(path.split('.')[:-1])
        self.savePath = _path
        if ext == 'dat':
            _path = _path + '.txt'
            os.rename(path, _path)
            self.filePath = _path
            return True
        elif ext == 'txt':
            self.filePath = path
            return True
        else:
            return 'Dismatched file extension'
        
    def setSavePath(self, path):
        os.makedirs(path, exist_ok=True)
        self.savePath = path + '/' + '.'.join(self.filePath.split('/')[-1].split('.')[:-1])
        return True
        
    def setOriginDF(self):
        if self.filePath == None:
            return 'No file'
        
        self.originDF = makeOriginDF(self.filePath)
        return True
    
    def setOptionAndCountDF(self):
        if self.filePath == None:
            return 'No file'
        if self.originDF is None:
            self.setOriginDF()
        
        self.optionDF, self.countDF = makeOptionAndCountDF(self.originDF)
        return True
    
    def getCountDF(self):
        if self.filePath == None:
            return 'No file'
        if self.countDF is None:
            self.setOptionAndCountDF()

        return self.countDF
    
    def setChoosedDF(self, choosedID=None):
        if self.filePath == None:
            return 'No file'
        if self.countDF is None:
            self.setOptionAndCountDF()
        if choosedID == None:
            choosedID = list(range(1,len(self.countDF)+1))

        self.choosedDF = makeChoosedDF(choosedID, self.countDF, self.optionDF)
        return True
    
    def saveDF(self, type='all'):
        filePath = self.savePath

        if type == 'origin' or type == 'all':
            if self.originDF is None: self.setOriginDF()
            self.originDF.to_csv(filePath + '(group).csv', index = False)

        if type == 'count' or type == 'all':
            if self.countDF is None: self.setOptionAndCountDF()
            self.countDF.to_csv(filePath + '(count).csv', index = False)

        if type == 'option' or type == 'all':
            if self.optionDF is None: self.setOptionAndCountDF()
            self.optionDF.to_csv(filePath + '(option).csv', index = False)

        if type == 'choosed' or type == 'all':
            if self.choosedDF is None: self.setChoosedDF()
            self.choosedDF.to_csv(filePath + '(choosed).csv', index = False)
        return True
  