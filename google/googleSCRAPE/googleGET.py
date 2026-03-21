import pandas as pd
from pytrends.request import TrendReq                      #module to request google trends
import os


pytrend = TrendReq()
us = pytrend.trending_searches(pn='united_states')
india = pytrend.trending_searches(pn='india')
philippines = pytrend.trending_searches(pn='philippines')
nigeria = pytrend.trending_searches(pn='nigeria')
uk = pytrend.trending_searches(pn='united_kingdom')
germany = pytrend.trending_searches(pn='germany')
canada = pytrend.trending_searches(pn='canada')
australia = pytrend.trending_searches(pn='australia')


allCountry = [us, india, philippines, nigeria, uk, germany, canada, australia]
allCountrySTR = ["united states", "india", "philippines", "nigeria", "united kingdom", "germany", "canada", "australia"]


count = 0 
current_dir = os.path.dirname(os.path.abspath(__file__))
fileWithTrending = open(os.path.join(current_dir, "googleTRENDING.txt"), "w")


for each in allCountry:

    temp = allCountrySTR[count] + ", "

    for every in each[0]:
        temp = temp + every + ", "

    fileWithTrending.write(temp + "\n" )
    count = count + 1

fileWithTrending.close() 

print("completed")
