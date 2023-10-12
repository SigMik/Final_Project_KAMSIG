from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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
df = pd.read_csv('csv_files/LKL_efficiency.csv')
wdf = pd.read_csv('csv_files/MLKL_efficiency.csv')

df['Resultefficiency']=df['Sum']/df['Games']
sortdf=df.sort_values(by='Resultefficiency', ascending=False).round(2)
# print(sortdf)
# #
# wdf['Resultefficiency']=wdf['Sum']/wdf['Games']
# sortwdf=wdf.sort_values(by='Resultefficiency', ascending=False).round(2)
# # print(sortwdf)
# #
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
## wdf = pd.read_csv('MLKL_efficiency.csv')


# df = pd.read_csv('csv_files/LKL_efficiency.csv')
# # df.Teamresultefficiency=df.groupby(["Team"]).sum()
# # print(df.Teamresultefficiency)
# #
# df['Result']=df['Sum']/df['Games']
# sortdf=df.sort_values(by='Result', ascending=False).round(2)
# groupsortdf = sortdf.groupby(["Team"]).sum()
#
# groupsortdf_barplot = groupsortdf.drop(columns = ['Place','Games','Sum','Unnamed: 0','Player'])
# print(groupsortdf_barplot)
#
# sns.barplot(data = groupsortdf_barplot, x= 'Team', y = 'Result')
# plt.title('LKL teams by efficiency in 2022-2023 season')
# plt.xlabel('Teams')
# plt.ylabel('Result')
# plt.show()

# ******

# BANDYMAS, ISTRINTI

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
# print(sortwdf)

# # Sukuriame su image diagramą
# img=[plt.imread('C:\FotoLKL\ImageLKL.png'), plt.imread('C:\FotoLKL\ImageMLKL.png')]
# plt.bar([0,1], [1,2])
# plt.xticks([0,1], ['',''])
#
# ax=plt.gca()
# tick_labels = ax.xaxis.get_ticklabels()
# for i,im in enumerate(img):
#     ib = OffsetImage(im, zoom=.4)
#     ib.image.axes = ax
#     ab = AnnotationBbox(ib,
#         tick_labels[i].get_position(),
#         frameon=False,
#         box_alignment=(1,1)
#     )
#     ax.add_artist(ab)
# print(ax)

# plt.figure(figsize=(6, 6))
# sns.barplot(data=sortdf[:1], x="Player", y="Result", hue='Result', color='black', width=0.2)
# sns.barplot(data=sortwdf[:1], x="Player", y="Result", hue='Result', color='black', width=0.2)
# plt.title("Best results of PTS average")
# plt.xlabel("LKL and MLKL player ")
# plt.ylabel("Result by PTS average 2022-2023 season")
# plt.show()


