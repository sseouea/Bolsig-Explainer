import pandas as pd

def findCols(line):
  cols = ['R#']
  for col in ['E/N (Td)', 'Energy (eV)']:
    if col in line:
      cols.append(col)
  cIdx = line.find('C')
  if cIdx == -1: cIdx = line.find('A')
  _col = line[cIdx:].split()
  cols = cols + _col

  return cols

def processEnergyLossCoeff(energyLossCoeff):
  df = energyLossCoeff.copy()
  _df = df.loc[:,df.columns[3:]]
  _df = _df.applymap(lambda x : 0 if x < 0 else x) ##
  df = pd.concat([df.loc[:,df.columns[:3]], _df], axis=1)

  return df

def calEnergyLossFraction(energyLossCoeff):
  df = energyLossCoeff.copy()
  _df = df.loc[:,df.columns[3:]]
  _df = _df.div(_df.sum(axis=1), axis=0)
  df = pd.concat([df.loc[:,df.columns[:3]], _df], axis=1)

  return df

