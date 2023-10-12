from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ******

# didziausią taškų vidurkį per sezono rungtynes pelnęs žaidėjas LKL ir MLKL

# df = pd.read_csv('LKL_points.csv')
# wdf = pd.read_csv('MLKL_points.csv')
#
# df['Result']=df['Sum']/df['Games']
# sortdf=df.sort_values(by='Result', ascending=False).round(2)
# print(sortdf)
#
# wdf['Result']=wdf['Sum']/df['Games']
# sortwdf=wdf.sort_values(by='Result', ascending=False).round(2)
# # print(sortwdf)
#
# # Sukuriame stulpelinę diagramą
# plt.figure(figsize=(6, 6))
# sns.barplot(data=sortdf[:1], x="Player", y="Result", hue='Result', color='black', width=0.2)
# sns.barplot(data=sortwdf[:1], x="Player", y="Result", hue='Result', color='black', width=0.2)
# plt.title("Best results of PTS average")
# plt.xlabel("LKL and MLKL player ")
# plt.ylabel("Result by PTS average 2022-2023 season")
# plt.show()

# ******

# penki žaidėjai pagal didžiausius efektyvumo balus LKL ir MLKL
#
# df = pd.read_csv('LKL_efficiency.csv')
# wdf = pd.read_csv('MLKL_efficiency.csv')
#
# df['Resultefficiency']=df['Sum']/df['Games']
# sortdf=df.sort_values(by='Resultefficiency', ascending=False).round(2)
# # print(sortdf)
#
# wdf['Resultefficiency']=wdf['Sum']/wdf['Games']
# sortwdf=wdf.sort_values(by='Resultefficiency', ascending=False).round(2)
# # print(sortwdf)
#
# sns.set_theme(style='whitegrid')
# plt.figure(figsize=(12, 8))
# sns.barplot(data=sortdf[:3], x="Player", y="Resultefficiency", hue = 'Team', palette = 'dark', alpha =.4)
# sns.barplot(data=sortwdf[:3], x="Player", y="Resultefficiency", hue = 'Team', palette = "dark", alpha =.4)
# plt.title("Best three by efficiency points 2022-2023 season")
# plt.xlabel("LKL and MLKL player ")
# plt.ylabel("Efficiency points by players")
# plt.show()

# ******

# komandų pasiskirstymas pagal efektyvumo balą LKL ir MLKL

df = pd.read_csv('LKL_efficiency.csv')
# wdf = pd.read_csv('MLKL_efficiency.csv')

df.Teamresultefficiency=df.groupby(["Team"]).sum()
print(df.Teamresultefficiency)












