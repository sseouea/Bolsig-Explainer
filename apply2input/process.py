import pandas as pd
import platform

'''
Below lines shows the example data of Bolsig+ Input Data, the cross section data.
The cross section data includes various information. So, here the discription of the data.
There are various options in first line. Those are 'ELASTIC', 'EFFECTIVE', 'MOMENTUM', 'IONIZATION', 'ATTACHMENT'
and 'EXCITATION'. Short but strong words each explains the situation of each cases. For example, the 'IONIZATION'
means that 2 electrons be fall off from the atom/molecule because of the collision. We will call those as 'state'.
Second line, 'b', is the simple discription of the case and it can be classified into two types: unidirectional arrow and bidirectional arrow.
The case 2 indicates the bidirectional type. Simple, in case 2, the N2 and electron collide and N2 be the N2(V1).
In this case, the N2(V1) is 'EXCITATION' state so it can easily be N2. By this, not only '->' but also '<-'.
Therefore, combining those, the arrow expressed as '<->'. The third row, 'c', is the threshold energy and it be specified on
'e' and 'f' sometimes. The fourth line shows the species which be collide and fifth line indicates the process,
what happens on that case. The sixth line is parameters. Other lines are some additional information.

| id || state || equation || value || species || process || param. || comment || updated |

(case1) : unidirectional arrow
a. ELASTIC
b. N2 -> N2
c. 1.950000e-5
d. SPECIES: e / N2
e. PROCESS: E + N2 -> E + N2, Elastic
f. PARAM.:  m/M = 0.0000195, complete set
g. COMMENT: elastic MOMENTUM-TRANSFER CROSS SECTION.
h. UPDATED: 2012-10-11 09:34:55

(case2) : bidirectional arrow
a'. EXCITATION
b'. N2 <-> N2(V1)
c'.  2.889000e-1
d'. SPECIES: e / N2
e'. PROCESS: E + N2 -> E + N2( VIB V1), Excitation
f'. PARAM.:  E = 0.2889 eV, complete set
g'. UPDATED: 2012-10-11 09:34:55
h'. COLUMNS: Energy (eV) | Cross section (m2)
'''

def processInput(filePath):
    # make .csv with input file (.txt / .dat)

    # check the extension of file
    ################################################
    extension = filePath.split('.')[-1]
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

    state = ['ELASTIC', 'EFFECTIVE', 'MOMENTUM', 'IONIZATION', 'ATTACHMENT', 'EXCITATION']
    columns = ['state', 'equation', 'value', 'species', 'process', 'param.', 'comment', 'updated']

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

                
