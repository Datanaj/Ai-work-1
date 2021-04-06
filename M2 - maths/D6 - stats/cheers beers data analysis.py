import pandas as pd
import numpy as np
from urllib.request import urlretrieve
# step 1: read the data file
URL = 'http://go.gwu.edu/engcomp2data1'
urlretrieve(URL, 'beers.csv')
beers = pd.read_csv("beers.csv")
#print(type(beers))
#print(beers.head())


# step 2 : explore data

# isolating style column for exploring
beers['style']
styletype = beers.dtypes['style']
#print(styletype)

# exploring and cleaning the abv and ibu columns
#print(beers['abv'].head(10))
abv_series = beers['abv']
#print(len(abv_series))
abv_series_clean = abv_series.dropna()
#print(abv_series)
#print(len(abv_series_clean))
ibu_series = beers['ibu']
ibu_series_clean = ibu_series.dropna()
#print(len(ibu_series))
#print(len(ibu_series_clean))

# created function to calculate percentage change of clean data compared to original data in column
def percent(clean,total):
    percentage = (clean/total)*100
    print(percentage)

print(percent(len(ibu_series_clean), len(ibu_series)))






