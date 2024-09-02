# Bolsig+ | Explainer

made by. Seohyun Kim & Chanhyeok Kim </br>
email. sseouea03@gmail.com

## Introduction

The program is for processing the .csv / .dat file using on Bolsig+ including input and output file both of all.
- **input file** : cross section
- **output file** : input cross section, conditions, rate coefficients, inverse rate coefficients, transport coefficients (+ energy loss coefficients)
  - ```Energy loss coefficients``` : exactly not included on output file, the program automatically calculate the value through given data (rate coefficients)
 
## Result

Basically, the result files be created in the folder which is in the same location with the give (input / output) file. Also, the name of the folder is same with the given (input / output) file.

### [1] Input File

Four files (.csv) be made as a results.

1. **--file name--**``(group)``.csv
- The information of elements in input file.
- No processing, just make it into the .csv file.

2. **--file name--**``(count)``.csv
- The option (species - # of species) which Bolsig+ recognized in given input file.


3. **--file name--**``(option)``.csv
- Add column 'option1' and 'option2' in the **--file name--**``(group)``.csv.
- The option means what species the element belongs to based on rule of Bolsig+.
- One element belongs to minimum 1 species, maximum 2 species.

4. **--file name--**``(choosed)``.csv
- The elements which be used in Bolsig+ depends on your species selection.
- If one elements is corresponds to several species then it can be appear several times. (one time for one species)
- The 'id' of element is same with 'id' in **--file name--**``(option)``.csv.


### [2] Output File

Select the desired data which you want to process into .csv file.
- 'Input cross section' and 'Conditions' are not supported yet.
- / expressed as ; in file name

1. **--file name--**``(Energy loss coefficients (eV m3;3))``.csv
2. **--file name--**``(Energy loss fractions)``.csv
3. **--file name--**``(Inverse rate coefficients (m3;s))``.csv
4. **--file name--**``(Rate coefficients (m3;s))``.csv
5. **--file name--**``(Transport coefficients)``.csv
