from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# didziausią taškų vidurkį per sezono rungtynes pelnęs žaidėjas LKL ir MLKL
df = pd.read_csv('LKL_points.csv')
df1 = pd.read_csv('MLKL_points.csv')

df['Result']=df['Sum']/df['Games']
sortdf=df.sort_values(by='Result', ascending=False)
# print(sortdf)

df1['Result']=df1['Sum']/df['Games']
sortdf1=df1.sort_values(by='Result', ascending=False)
print(sortdf1)





























