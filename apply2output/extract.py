import pandas as pd
from utills import *

def getCrossSection(params):
  # data is already in input file
  # difference with input file : 'Extra points added by BOLSIG+:'

  lineIdx, lines = params

  while True:
    line = lines[lineIdx].strip()
    if line == '': break

    lineIdx += 1

  return None, lineIdx

def getCondition(params):
  lineIdx, lines = params
  lineIdx += 1
  results = [None, None]

  cols = ['A', 'condition', 'value']
  data = {col : list() for col in cols}
  while True:
    line = lines[lineIdx].strip()

    if line[0] != 'A': break
    line = line.split()
    try:
      _ = float(line[-1])
      line = [line[0]] + [' '.join(line[1:-1])] + [line[-1]]
    except:
      line = [line[0]] + [' '.join(line[1:])]

    for idx, col in enumerate(cols):
      if idx >= len(line):
        data[col].append(None)
      else:
        data[col].append(line[idx])

    lineIdx += 1
  results[0] = pd.DataFrame(data)

  # ex) R# A1 A16 A17
  cols = line.split()
  lineIdx += 1
  data = {col : list() for col in cols}
  while True:
    line = lines[lineIdx].strip()

    if line == '': break
    line = line.split()

    for idx, col in enumerate(cols):
      data[col].append(line[idx])

    lineIdx += 1
  results[1] = pd.DataFrame(data)

  return results, lineIdx

def getCoeff(params):
  lineIdx, lines = params
  lineIdx += 1

  while True:
    line = lines[lineIdx].strip()

    if line[0] == 'R': break
    lineIdx += 1

  cols = findCols(line)
  lineIdx += 1
  data = {col : list() for col in cols}
  while True:
    line = lines[lineIdx].strip()

    if line == '': break
    line = line.split()

    for idx, col in enumerate(cols):
      data[col].append(line[idx])

    lineIdx += 1

  data = pd.DataFrame(data, dtype='float64')
  return data, lineIdx