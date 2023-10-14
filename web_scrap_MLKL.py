from bs4 import BeautifulSoup
import requests
import pandas as pd

# mdata=[]
# # #issirenkam pagal pelnomus taskus ir 2022-2023 sezona
# url = ('https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&'
#        'stage=0&fpos=pts&sort=total&games_type=all')
# response = requests.get(url)
# # # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
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
#
# df=pd.DataFrame(mdata)
# print(df)

# df.to_csv('MLKL_points.csv')

#******

# mdata1=[]
# #issirenkam pagal atkovotus kamuolius ir 2022-2023 sezona
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=reb&sort=total&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

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
#         mdata1.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum
#         })
#
# df=pd.DataFrame(mdata1)
# print(df)
#
# df.to_csv('MLKL_rebounds.csv')

#******

# mdata2=[]
# #issirenkam pagal rezultatyvius perdavimus ir 2022-2023 sezona
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=as&sort=total&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

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
#         mdata2.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum
#         })
#
# df=pd.DataFrame(mdata2)
# print(df)
#
# df.to_csv('MLKL_assists.csv')

#******

# mdata3=[]
# #issirenkam pagal naudinguma rezultatyvius perdavimus ir 2022-2023 sezona
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=eff&sort=total&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
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
#
# df=pd.DataFrame(mdata3)
# print(df)
#
# df.to_csv('MLKL_efficiency.csv')

# ******

# mdata4=[]
# #issirenkam pagal tritaskiu metimo taikluma ir 2022-2023 sezona
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=3pts&sort=average&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
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
#             three_pts_percentage = columns[2].text.strip()
#         except IndexError:
#             three_pts_percentage = ""
#
#         mdata4.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Three_pts_percentage': three_pts_percentage
#         })
#
# df=pd.DataFrame(mdata4)
# print(df)
#
# df.to_csv('MLKL_3_points_percentage.csv')

# ******
#
# wdata2022_2023=[] #MLKL points in 2022-2023 season
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=pts&sort=total&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# table=soup.find('table',class_='list02')
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             place = columns[0].text.strip().replace('.', '')
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
#         wdata2022_2023.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum,
#             'Season': '2022-2023'
#         })
#
# df2022_2023=pd.DataFrame(wdata2022_2023)
# # print(df2022_2023)
#
# # ******
#
# wdata2021_2022=[] #MLKL points in 2021-2022 season
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2021&fmonth=0&stage=0&fpos=pts&sort=total&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# table=soup.find('table',class_='list02')
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             place = columns[0].text.strip().replace('.', '')
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
#         wdata2021_2022.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum,
#             'Season': '2021-2022'
#         })
#
# df2021_2022=pd.DataFrame(wdata2021_2022)
# # print(df2021_2022)
#
# # ******
#
# wdata2020_2021=[] #MLKL points in 2020-2021 season
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2020&fmonth=0&stage=0&fpos=pts&sort=total&games_type=all'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# table=soup.find('table',class_='list02')
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             place = columns[0].text.strip().replace('.', '')
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
#         wdata2020_2021.append({
#             'Place': place,
#             'Player': player,
#             'Team': team,
#             'Games': games,
#             'Sum': sum,
#             'Season': '2020-2021'
#         })
#
# df2020_2021=pd.DataFrame(wdata2020_2021)
# # print(df2020_2021)
#
# S3_MLKL_points = pd.concat([df2022_2023, df2021_2022, df2020_2021])
# print(S3_MLKL_points)
#
# S3_MLKL_points.to_csv('S3_MLKL_points.csv')