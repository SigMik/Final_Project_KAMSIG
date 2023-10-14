from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# ******

# CALCULIATION FOR INDEXES AND VIZUALIZATION FOR HIGHEST RESULT PLAYERS"
#
# df = pd.read_csv('csv_files/LKL_points.csv')
# wdf = pd.read_csv('csv_files/MLKL_points.csv')
#
# df['Result']=df['Sum']/df['Games']
# sortdf=df.sort_values(by='Result', ascending=False).round(2)
# print(sortdf)
#
# wdf['Result']=wdf['Sum']/df['Games']
# sortwdf=wdf.sort_values(by='Result', ascending=False).round(2)
# print(sortwdf)
#
# # Sukuriame stulpelinę diagramą
# plt.figure(figsize=(6, 6))
# sns.barplot(data=sortdf[:1], x="Player", y="Result", hue='Result', palette='dark:white', width=0.2)
# sns.barplot(data=sortwdf[:1], x="Player", y="Result", hue='Result', palette='dark:red', width=0.2)
# plt.title("Highest results of points per games in 2022-2023 season")
# plt.text(0.15, 17, 'Ahmad Caver')
# plt.text(0.4, 10, 'Tyra Marie Buss')
# plt.xticks(fontsize = 0)
#
# img=[plt.imread('C:\FotoLKL\ImageLKL1.png'), plt.imread('C:\FotoLKL\ImageMLKL2.png')]
#
# ax=plt.gca()
# tick_labels = ax.xaxis.get_ticklabels()
# for i,im in enumerate(img):
#     ib = OffsetImage(im, zoom=.4)
#     ib.image.axes = ax
#     ab = AnnotationBbox(ib,
#         tick_labels[i].get_position(),
#         frameon=False,
#         box_alignment=(-0.25,-0.2)
#     )
#     ax.add_artist(ab)
# plt.xlabel('Player')
# plt.ylabel("Result by PTS average")
# ##plt.savefig('Highest results players.png')
# plt.show()

# ******

### CALCULIATION FOR INDEXES AND VIZUALISATION FOR EFFICIENCY POINTS BY PLAYERS

# df = pd.read_csv('csv_files/LKL_efficiency.csv')
# wdf = pd.read_csv('csv_files/MLKL_efficiency.csv')
#
# df['Resultefficiency']=df['Sum']/df['Games']
# sortdf=df.sort_values(by='Resultefficiency', ascending=False).round(2)
# print(sortdf)
#
# wdf['Resultefficiency']=wdf['Sum']/wdf['Games']
# sortwdf=wdf.sort_values(by='Resultefficiency', ascending=False).round(2)
# # print(sortwdf)
#
# sns.set_theme(style='whitegrid')
# plt.figure(figsize=(10, 8))
# sns.barplot(data=sortdf[:3], x="Player", y="Resultefficiency", hue = 'Team', palette = 'Greens_d', alpha =.4)
# sns.barplot(data=sortwdf[:3], x="Player", y="Resultefficiency", hue = 'Team', palette = "Greens_d", alpha =.4)
# plt.title("Best three LKL and MLKL players by efficiency points 2022-2023 season")
# plt.xlabel("LKL and MLKL player ")
# plt.ylabel("Efficiency points by players")
# ###plt.savefig('EFF points by players in LKL and MLKL')
# plt.show()

# ******

# # komandų pasiskirstymas pagal efektyvumo balą LKL

# df = pd.read_csv('csv_files/LKL_efficiency.csv')
#
# df['Result']=df['Sum']/df['Games']
# sortdf=df.sort_values(by='Result', ascending=False).round(2)
# groupsortdf = sortdf.groupby(["Team"]).sum()
#
# groupsortdf_barplot = groupsortdf.drop(columns = ['Place','Games','Sum','Unnamed: 0','Player'])
# sorted_by_asc = groupsortdf_barplot.sort_values('Result')
# # print(groupsortdf_barplot)
# print(sorted_by_asc)
#
# sns.set_style("darkgrid", {"grid.color": ".10", "grid.linestyle": ":"})
# sns.barplot(data = sorted_by_asc, x= 'Team', y = 'Result')
# plt.title('LKL teams efficiency per game in 2022-2023 season')
# plt.text(0.0, 63, 'Gargždai', rotation=90, fontsize = 10)
# plt.text(0.9, 80, 'CBet', rotation=90, fontsize = 10)
# plt.text(1.9, 75, 'Neptūnas', rotation=90, fontsize = 10)
# plt.text(3, 58, 'Pieno žvaigždės', rotation=90, fontsize = 10)
# plt.text(4, 88, 'Šiauliai', rotation=90, fontsize = 10)
# plt.text(5, 68, '7bet-Lietkabelis', rotation=90, fontsize = 10)
# plt.text(6, 78, 'Labas Gas', rotation=90, fontsize = 10)
# plt.text(7, 75, 'Nevėžis–Optibet ', rotation=90, fontsize = 10)
# plt.text(8, 110, 'Wolves', rotation=90, fontsize = 10)
# plt.text(9, 75, 'Uniclub Casino - Juventus', rotation=90, fontsize = 10)
# plt.text(9.9, 130, 'Žalgiris ', rotation=90, fontsize = 10)
# plt.text(11, 140, 'Rytas', rotation=90, fontsize = 10)
# plt.xticks(fontsize = 0)
# plt.xlabel('Teams')
# plt.ylabel('Result per game')
### plt.savefig('LKL teams EFF 2022-2023.png')
# # plt.show()

# ******

# komandų pasiskirstymas pagal efektyvumo balą MLKL

# wdf = pd.read_csv('csv_files/MLKL_efficiency.csv')
#
# wdf['Result']=wdf['Sum']/wdf['Games']
# wsortdf=wdf.sort_values(by='Result', ascending=False).round(2)
# wgroupsortdf = wsortdf.groupby(["Team"]).sum()
#
# wgroupsortdf_barplot = wgroupsortdf.drop(columns = ['Place','Games','Sum','Unnamed: 0','Player'])
# wsorted_by_asc = wgroupsortdf_barplot.sort_values('Result')
# # print(groupsortdf_barplot)
# print(wsorted_by_asc)
#
# plt.figure(figsize=(8, 8))
# sns.set_style("darkgrid", {"grid.color": ".10", "grid.linestyle": ":"})
# plots = sns.barplot(x="Team", y="Result", data=wsorted_by_asc, color ='grey')
# for bar in plots.patches:
#     plots.annotate(format(bar.get_height(), '.2f'),
#                    (bar.get_x() + bar.get_width() / 2,
#                     bar.get_height()), ha='right', va='center',
#                    size=14, xytext=(0, 8),
#                    textcoords='offset points')
# plt.xlabel("Team", size=14)
#
# plt.ylabel("Result", size=14)
# plt.title("MLKL teams efficiency per game in 2022-2023 season", fontsize=15)
# plt.text(0.2, 10, 'Šiaulių Šiauliai-Vilmers', rotation=90, fontsize = 12)
# plt.text(1.2, 4, 'Klaipėdos LCC tarptautinis universitetas', rotation=90, fontsize = 12)
# plt.text(2.2, 38, 'Kauno Aistės-LSMU ', rotation=90, fontsize = 12)
# plt.text(3.2, 43, 'Klaipėdos Neptūnas ', rotation=90, fontsize = 12)
# plt.text(4.2, 100, 'Vilniaus Kibirkštis ', rotation=90, fontsize = 12)
# plt.xticks(fontsize = 0)
# plt.xlabel('Teams')
# plt.ylabel('Efficiency points per game')
# ##plt.savefig('MLKL teams EFF 2022-2023.png')
# plt.show()

# ******

# LKL komandų rezultatai pagal komandos rungtynių taškų vidurkį per trejus sezonus

# df = pd.read_csv('csv_files/BS3_LKL_points.csv')
#
# dfbasic = df.drop(columns = ['Unnamed: 0'])
# dfbasicsor = dfbasic.sort_values('Season')
# # print(dfbasic)
# print(dfbasicsor)
#
# sns.set_style("whitegrid", {
#   "ytick.major.size": 0.1,
#     "ytick.minor.size": 0.05,
#    'grid.linestyle': 'dashed',
#  })
# g = sns.lineplot(data=dfbasicsor, x="Season", y="Avg", hue='Team')
# lines = g.get_lines()
# g.legend(fontsize="5", loc ="lower left")
# plt.title('LKL teams variation during 3 seasons')
# plt.xlabel('Seasons')
# plt.ylabel('Point average during game')
# ##plt.savefig('LKL teams variation 3 seasons.png')
# plt.show()
