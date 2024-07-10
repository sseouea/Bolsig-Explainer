import pandas as pd

def findOption(eq):
  option = None

  if '<->' in eq:
    idx = eq.find('<')
    option = [eq[:idx].strip(), eq[idx+3:].strip()]
  elif '->' in eq:
    idx = eq.find('>')
    option = [eq[:idx-1].strip()]
  else:
    option = [eq.strip()]

  return option

def makeOptionAndCountDF(df):
    optionDf = df.copy()
    countData = dict()

    for idx, row in optionDf.iterrows():
        options = findOption(row['equation'])

        for i, option in enumerate(options):
            if option in countData:
                countData[option] += 1
            else:
                countData[option] = 1

            optionDf.loc[idx, f'option{i+1}'] = option

    _countData = {'option' : list(countData.keys()), 'count' : list(countData.values())}
    countDf = pd.DataFrame(_countData)
    countDf['id'] = countDf.index + 1
    countDf.insert(0, 'id', countDf.pop('id'))

    return optionDf, countDf