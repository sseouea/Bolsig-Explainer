import pandas as pd

def makeOriginDF(filePath):
    state = ['ELASTIC', 'EFFECTIVE', 'MOMENTUM', 'IONIZATION', 'ATTACHMENT', 'EXCITATION']
    columns = ['state', 'equation', 'value', 'species', 'process', 'param.', 'comment', 'updated']

    f = open(filePath, 'r')
    data = {c : list() for c in columns}

    lines = f.readlines()
    lineIdx = 0

    while lineIdx < len(lines):
        line = lines[lineIdx]
        line = line.strip()

        if line in state:
            exist = {c : 0 for c in columns}

            for i in range(3):
                if ':' in line: break
                data[columns[i]].append(line)
                exist[columns[i]] = 1

                lineIdx += 1
                line = lines[lineIdx].strip()

            while True:
                if 'COLUMNS' in line:
                    break

                idx = line.find(':')
                key = line[:idx].strip().lower()
                val = line[idx+1:].strip()

                if len(data['state']) == len(data[key]):
                    data[key][-1] = data[key][-1] + ' ' + val
                else:
                    data[key].append(val)
                    exist[key] = 1

                lineIdx += 1
                line = lines[lineIdx].strip()

            for c in columns:
                if exist[c] == 0:
                    data[c].append('')

        lineIdx += 1
    
    f.close()

    df = pd.DataFrame(data)
    df['id'] = df.index + 1
    df.insert(0, 'id', df.pop('id'))

    return df

                
