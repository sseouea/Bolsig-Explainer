from DFmanager import *

if __name__ == '__main__':
    inputPath = './input/input.txt'
    outputPath = './output'

    manager = DFmanager()
    manager.setFilePath(inputPath)
    manager.setSavePath(outputPath)
    manager.saveDF()
