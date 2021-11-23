import pandas as pd
from pytrends.request import TrendReq                      #module to request google trends


pytrend = TrendReq()

us = pytrend.trending_searches(pn='united_states')
india = pytrend.trending_searches(pn='india')
philippines = pytrend.trending_searches(pn='philippines')
nigeria = pytrend.trending_searches(pn='nigeria')
uk = pytrend.trending_searches(pn='united_kingdom')
germany = pytrend.trending_searches(pn='germany')
canada = pytrend.trending_searches(pn='canada')
australia = pytrend.trending_searches(pn='australia')


allcountry = [us, india, philippines, nigeria, uk, germany, canada, australia]
allcountrySTR = ["united states", "india", "philippines", "nigeria", "united kingdom", "germany", "canada", "australia"]

count = 0 
fileTREND = open("Google-Trending/google/googleSCRAPE/googleTRENDING.txt","w")

for each in allcountry:

    temp = allcountrySTR[count] + ", "
    count = count + 1

    for every in each[0]:
        temp = temp + every + ", "

    fileTREND.write(temp + "\n" )
        
fileTREND.close() 

print("completed")
