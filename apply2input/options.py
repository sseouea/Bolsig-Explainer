import pandas as pd

'''
| id || option || count |

| <- ... -> || option1 || option2 |
- each case has 1 (unidirectional arrow) or 2(bidirectional arrow)
'''

def identifyOptions(eq):
  # identify options from given equation

  '''
  case1. A -> B
  species) A

  case2. A <-> B
  species) A, B
  '''

  options = None

  if '<->' in eq:
    idx = eq.find('<')
    options = [eq[:idx].strip(), eq[idx+3:].strip()]
  elif '->' in eq:
    idx = eq.find('>')
    options = [eq[:idx-1].strip()]
  else:
    options = [eq.strip()]

  return options


def getOptionsInfo(df):
    # add option information in table
    # make table which has information about each option's number

    newDF = df.copy()
    countData = dict()

    for idx, row in newDF.iterrows():
        options = identifyOptions(row['equation'])

        for i, option in enumerate(options):
            if option in countData:
                countData[option] += 1
            else:
                countData[option] = 1

            newDF.loc[idx, f'option{i+1}'] = option

    _countData = {'option' : list(countData.keys()), 'count' : list(countData.values())}
    countDF = pd.DataFrame(_countData)
    countDF['id'] = countDF.index + 1
    countDF.insert(0, 'id', countDF.pop('id'))

    return newDF, countDF