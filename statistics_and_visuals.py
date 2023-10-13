from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# ******

# didziausią taškų vidurkį per sezono rungtynes pelnęs žaidėjas LKL ir MLKL
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
# sns.barplot(data=sortwdf[:1], x="Player", y="Result", hue='Result', palette='dark:white', width=0.2)
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
# plt.savefig('Highest results players.png')
# plt.show()

# ******

# trys žaidėjai pagal didžiausius efektyvumo balus LKL ir MLKL 2022-2023 sezone

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
# plt.figure(figsize=(12, 8))
# sns.barplot(data=sortdf[:3], x="Player", y="Resultefficiency", hue = 'Team', palette = 'dark', alpha =.4)
# sns.barplot(data=sortwdf[:3], x="Player", y="Resultefficiency", hue = 'Team', palette = "dark", alpha =.4)
# plt.title("Best three LKL and MLKL players by efficiency points 2022-2023 season")
# plt.xlabel("LKL and MLKL player ")
# plt.ylabel("Efficiency points by players")
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
# plt.show()

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
# sns.set_theme(style='whitegrid')
# plt.figure(figsize=(8, 6))
# sns.barplot(data=wsorted_by_asc, x="Team", y="Result", hue = 'Team', palette = 'dark', alpha =.4)
# plt.title('MLKL teams efficiency per game in 2022-2023 season')
# plt.xticks(rotation = 8, size = 7)
# plt.xlabel('Teams')
# plt.ylabel('Result per game')
# plt.savefig('MLKL teams EFF 2022-2023.png')
# plt.show()

# ******

# pasirinktos komandos pokytis per tris sezonus NEPAVYKSTA, BANDYTI TOLIAU

df = pd.read_csv('csv_files/S3_LKL_points.csv')

df['Result']=df['Sum']/df['Games']
sortdf=df.sort_values(by='Result', ascending=False).round(2)
groupsortdf = sortdf.groupby(["Team"]).sum()

groupsortdf_bar = groupsortdf.drop(columns = ['Place','Games','Sum','Unnamed: 0','Player'])
gruopsortdf_bar1 = groupsortdf_bar.groupby(['Team','Season']) ['Result'].sum()
# sorted_by_asc = groupsortdf_bar.sort_values('Result')
# print(groupsortdf_bar)
print(gruopsortdf_bar1)
# print(sorted_by_asc)


# plt.figure(figsize=(12,8))
# plt.plot
# plt.xlabel(df['Season'])
# plt.ylabel('Amziauskai')
# plt.title('Mano pavyko Amzius pagal vardus')
# plt.show()

# ******

# tritaškių pataikymo procentas LKL ir MLKL

# df = pd.read_csv('csv_files/LKL_3_points_percentage.csv')
# # print(df)
# wdf = pd.read_csv('csv_files/MLKL_3_points_percentage.csv')
# # print(wdf)
#
# avg_3_percentage =df['Three_pts_percentage'].replace('%','').replace('.','').mean()
# print(avg_3_percentage)