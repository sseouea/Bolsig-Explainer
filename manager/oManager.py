import os
from pathlib import Path
import pandas as pd
from ..utils import *

class oManager:
    def __init__(self):
        # FilePath
        self.filePath = None
        self.savePath = None

        # DataFrame
        self.processedDF = None

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
            self.setProcessedDF()
        return True
        
    def setSavePath(self, path):
        self.savePath = path
        return True
    
    # 2. Manage DataFrame

    def setProcessedDF(self):
        if self.filePath == None:
            raise Exception('EmptyFilePathError')
        
        self.processedDF = processOutput(self.filePath)
        return True
    
    # 3. Save DataFrame

    def saveDF(self, type='all'):
        if self.savePath == None:
            raise Exception('EmptyFilePathError')
        if self.processedDF == None:
            self.setProcessedDF()
        
        filePath = self.savePath
        os.makedirs('/'.join(filePath.split('/')[:-1]), exist_ok=True)

        if type == 'all':
            for key in self.processedDF.keys:
                self.processedDF[key].to_csv(self.savePath + f'{key}.csv', index = False)
        else:
            if type not in self.processedDF.keys:
                raise Exception('InvalidKeyError')
            self.processedDF[type].to_csv(self.savePath + f'{type}.csv', index = False)

        return True
  