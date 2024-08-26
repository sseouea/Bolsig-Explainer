import os
from pathlib import Path
import pandas as pd
from ..utils import *

class iManager:
    def __init__(self):
        # FilePath
        self.filePath = None
        self.savePath = None

        # DataFrame
        self.originDF = None
        self.countDF = None
        self.optionDF = None
        self.choosedDF = None

    # 1. Manage File/Save Path

    def getFilePath(self):
        if self.filePath == None:
            raise Exception('EmptyVariableAccessError')
        return self.filePath
    
    def getSavePath(self):
        if self.savePath == None:
            raise Exception('EmptyVariableAccessError')
        return self.savePath

    def setFilePath(self, path):
        # if filePath is already exist, the content of dataframe have to be change
        ################################################
        if self.filePath != None:
            change = True
        else:
            change = False
        ################################################

        if not os.path.exists(path):
            raise Exception('InvalidFilePathError')
        
        ext = path.split('.')[-1]
        _path = '.'.join(path.split('.')[:-1])
        self.savePath = _path
        if ext == 'dat':
            _path = _path + '.txt'
            os.rename(path, _path)
            self.filePath = _path
        elif ext == 'txt':
            self.filePath = path
        else:
            raise Exception('InvalidFileExtensionError')
        
        if change == True:
            self.setOriginDF()
            self.setOptionAndCountDF()
        return True
        
    def setSavePath(self, path):
        self.savePath = path
        return True
        
    # 2. Manage DataFrame

    def setOriginDF(self):
        if self.filePath == None:
            raise Exception('EmptyFilePathError')
        
        self.originDF = processInput(self.filePath)
        return True
    
    def setOptionAndCountDF(self):
        if self.filePath == None:
            raise Exception('EmptyFilePathError')
        if self.originDF is None:
            self.setOriginDF()
        
        self.optionDF, self.countDF = getOptionsInfo(self.originDF)
        return True
    
    def getCountDF(self):
        if self.filePath == None:
            raise Exception('EmptyFilePathError')
        if self.countDF is None:
            self.setOptionAndCountDF()

        return self.countDF
    
    def setChoosedDF(self, choosedID=None):
        if self.filePath == None:
            raise Exception('EmptyFilePathError')
        if self.countDF is None:
            self.setOptionAndCountDF()
        if choosedID == None:
            choosedID = list(range(1,len(self.countDF)+1))

        self.choosedDF = getChosenInfo(choosedID, self.countDF, self.optionDF)
        return True
    
    # 3. Save DataFrame

    def saveDF(self, type='all'):
        if self.savePath == None:
            raise Exception('EmptyFilePathError')
        
        os.makedirs('/'.join(self.savePath.split('/')[:-1]), exist_ok=True)

        if type == 'origin' or type == 'all':
            if self.originDF is None: self.setOriginDF()
            self.originDF.to_csv(self.savePath + '(group).csv', index = False)

        if type == 'count' or type == 'all':
            if self.countDF is None: self.setOptionAndCountDF()
            self.countDF.to_csv(self.savePath + '(count).csv', index = False)

        if type == 'option' or type == 'all':
            if self.optionDF is None: self.setOptionAndCountDF()
            self.optionDF.to_csv(self.savePath + '(option).csv', index = False)

        if type == 'choosed' or type == 'all':
            if self.choosedDF is None: self.setChoosedDF()
            self.choosedDF.to_csv(self.savePath + '(choosed).csv', index = False)
        return True
  