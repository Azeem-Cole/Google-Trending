from collections import Counter
from datetime import datetime

allTrend = [[],[],[],[],[],[],[],[]]
count = 0

file = open("googleTRENDING.txt", "r")

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

for line in file:
    allTrend[count] = line.split(',')
    del allTrend[count][-1]
    count = count + 1

file.close()

countryUSA = allTrend[0]
countryINDIA= allTrend[1]
countryPHILIPPINES = allTrend[2]
countryNIGERIA = allTrend[3]
countryUK = allTrend[4]
countryGERMANY = allTrend[5]
countryCANADA = allTrend[6]
countryAUSTRALIA = allTrend[7]

dictUSA = dict(zip(countryUSA, range(162, 0, -1)))
dictINDIA = dict(zip(countryINDIA, range(142, 0, -1)))
dictPHILIPPINES = dict(zip(countryPHILIPPINES, range(122, 0, -1)))
dictNIGERIA = dict(zip(countryNIGERIA, range(102, 0, -1)))
dictUK = dict(zip(countryUK, range(82, 0, -1)))
dictGERMANY = dict(zip(countryGERMANY, range(62, 0, -1)))
dictCANADA = dict(zip(countryCANADA, range(42, 0, -1)))
dictAUSTRALIA = dict(zip(countryAUSTRALIA, range(22, 0, -1)))


dictUSA.pop("united states")
dictINDIA.pop("india")
dictPHILIPPINES.pop("philippines")
dictNIGERIA.pop("nigeria")
dictUK.pop("united kingdom")
dictGERMANY.pop("germany")
dictCANADA.pop("canada")
dictAUSTRALIA.pop("australia")

dictALL = Counter(dictUSA) + Counter(dictINDIA) + Counter(dictPHILIPPINES)  + Counter(dictNIGERIA) + Counter(dictUK) + Counter(dictGERMANY) + Counter(dictCANADA) + Counter(dictAUSTRALIA) 

sortALL = {}
for key, value in dictALL.items():
    sortALL[key] = value

finalDICT  = sorted(sortALL.items(), key=lambda x: x[1], reverse=True)

localtime = datetime.now() 

finalFILE = open(localtime.strftime("Yr%Y mth%m day%d"), "a")

finalFILE.write("Place".ljust(7) +"Score".ljust(7)+ "Term\n")

count = 1
for key in finalDICT:
    
    #finalFILE.write(((str(count).rjust(3) +", "+ key[0])) +.ljust(35)   +"\n")
    finalFILE.write(((str(count).ljust(7) + (str(key[1]).ljust(7)) + " "+ key[0])) +"\n")

    count = count + 1

finalFILE.close()
