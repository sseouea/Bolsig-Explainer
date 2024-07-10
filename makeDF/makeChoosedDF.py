import pandas as pd

def makeChoosedDF(choosedID, countDf, optionDf):
    choosedID.sort()
    choosedDf = pd.DataFrame()
    tempDf = None

    for idx in choosedID:
        option = countDf[countDf.id == idx].iloc[0]['option']

        tempDf = optionDf[(optionDf.option1 == option) | (optionDf.option2 == option)].copy()
        tempDf['criteria'] = option
        tempDf.insert(0, 'criteria', tempDf.pop('criteria'))

        choosedDf = pd.concat([choosedDf, tempDf])

    choosedDf.reset_index(drop=True, inplace=True)
    choosedDf['no'] = choosedDf.index + 1
    choosedDf.insert(0, 'no', choosedDf.pop('no'))

    return choosedDf