import pandas as pd

'''
| no || criteria || <- ... -> |

- no : the id of reaction in the Bolsig+
- criteria : how it be classified in the Bolsig+
'''

def getChosenInfo(choosedID, countDF, optionDF):
    choosedID.sort()
    choosedDF = pd.DataFrame()
    tempDF = None

    for idx in choosedID:
        option = countDF[countDF.id == idx].iloc[0]['option']

        tempDF = optionDF[(optionDF.option1 == option) | (optionDF.option2 == option)].copy()
        tempDF['criteria'] = option
        tempDF.insert(0, 'criteria', tempDF.pop('criteria'))

        choosedDF = pd.concat([choosedDF, tempDF])

    choosedDF.reset_index(drop=True, inplace=True)
    choosedDF['no'] = choosedDF.index + 1
    choosedDF.insert(0, 'no', choosedDF.pop('no'))

    return choosedDF