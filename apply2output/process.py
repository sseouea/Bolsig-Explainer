import pandas as pd
import platform
from extract import *

# return (a) data (b) finished line (included in dataframe)
def getData(dataType, lineIdx, lines):
  params = [lineIdx, lines]

  if dataType == 'Input cross section':
    return getCrossSection(params)
  elif dataType == 'Conditions':
    return getCondition(params)
  elif dataType in ['Rate coefficients (m3/s)', 'Inverse rate coefficients (m3/s)', 'Transport coefficients', 'Energy loss coefficients (eV m3/s)']:
    return getCoeff(params)
  else:
    raise Exception('InvalidDataFrameTypeError')

def processOnput(filePath):
    # make .csv with output file (.dat)

    # check the extension of file
    ################################################
    extension = filePath.split('.')
    if extension not in ['txt', 'dat']:
        raise Exception('InvalidFileExtensionError')
    ################################################

    # Window, Mac OS
    ################################################
    if (platform.system() == 'Windows'):
        f = open(filePath, 'r', encoding='utf-8')
    else:
        f = open(filePath, 'r')
    ################################################

    species = list()
    savedDataTypes = ['Collision input data', 'Input cross section', 'Conditions', 'Rate coefficients (m3/s)', 'Energy loss coefficients (eV m3/s)',
                  'Inverse rate coefficients (m3/s)', 'Transport coefficients']
    savedData = {dataType : None for dataType in savedDataTypes}
    conditionOptions = ['']

    f = open(filePath, 'r')
    dataType = None

    lines = f.readlines()
    lineIdx = 0

    while lineIdx < len(lines):
        # 'lineIdx' points the current line
        line = lines[lineIdx].strip() # current line

        if line == '':
            lineIdx += 1
            continue

        # Select the dataType
        if dataType == None:
            for _dataType in savedDataTypes:
                if _dataType in line:
                    dataType = _dataType
                    break

        # Construct the dataType
        if dataType != None:
            # start point : line where dataType is identified
            data = None
            if dataType == 'Collision input data':
                data = list()
                while True:
                    line = lines[lineIdx].strip()

                    if line == '': break
                    elif line == '-' * 50:
                        line = lines[lineIdx+1].strip()
                        lineIdx += 3

                        data.append(line)
                    else:
                        lineIdx += 1
            else:
                data, lineIdx = getData(dataType, lineIdx, lines)

            if dataType == 'Energy loss coefficients (eV m3/s)':
                data = processEnergyLossCoeff(data)
                savedData['Energy loss fractions'] = calEnergyLossFraction(data)
                
            savedData[dataType] = data
            dataType = None

        # Go to next line (after finished line)
        lineIdx += 1

    f.close()

    return savedData
        
