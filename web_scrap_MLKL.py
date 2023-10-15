from bs4 import BeautifulSoup
import requests
import pandas as pd

### MLKL WEB SCRAPING BY POINTS AND 2022-2023 SEASON
### creating emppty list for data storing
# mdata=[]
### scraping MLKL data by points category from chosen website
# url = ('https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&'
#        'stage=0&fpos=pts&sort=total&games_type=all')
### checking the URL response
# response = requests.get(url)
# # # print(response.status_code)

### getting needed data from URLs as table and indicating analysis method
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())

### extracting the data from the required table columns
# table=soup.find('table',class_='list02')
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             place = columns[0].text.strip()
#         except IndexError:
#             place = ""
#
#         try:
#             player = columns[1].text.strip()
#         except IndexError:
#             player = ""
#
#         try:
#             team = columns[3].text.strip()
#         except IndexError:
#             team = ""
#
#         try:
#             games = columns[4].text.strip()
#         except IndexError:
#             games = ""
#
#         try:
#             sum = columns[2].text.strip()
#         except IndexError:
#             sum = ""
#
#         mdata.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum
#         })

### creating DataFrame to store the collected data
# df=pd.DataFrame(mdata)
# print(df)

### exporting MLKL points data to csv file
# df.to_csv('MLKL_points.csv')

### MLKL WEB SCRAPING BY EFFICIENCY RATIO AND 2022-2023 SEASON
### creating emppty list for data storing
# mdata3=[]
### scraping MLKL data by efficiency ratio category from chosen website
# url = ('https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&'
#        'stage=0&fpos=eff&sort=total&games_type=all')
# response = requests.get(url)
### checking the URL response
# # print(response.status_code)
### getting needed data from URLs as table and indicating analysis method
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
### extracting the data from the required table columns
# table=soup.find('table',class_='list02')
#
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             place = columns[0].text.strip()
#         except IndexError:
#             place = ""
#
#         try:
#             player = columns[1].text.strip()
#         except IndexError:
#             player = ""
#
#         try:
#             team = columns[3].text.strip()
#         except IndexError:
#             team = ""
#
#         try:
#             games = columns[4].text.strip()
#         except IndexError:
#             games = ""
#
#         try:
#             sum = columns[2].text.strip()
#         except IndexError:
#             sum = ""
#
#         mdata3.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum
#         })

### creating DataFrame to store the collected data
# df=pd.DataFrame(mdata3)
# print(df)

### exporting MLKL efficiency data to csv file
# df.to_csv('MLKL_efficiency.csv')




