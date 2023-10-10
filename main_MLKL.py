from bs4 import BeautifulSoup
import requests
import pandas as pd

# mdata=[]
# #issirenkam pagal pelnomus taskus ir 2022-2023 sezona
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
#
# df=pd.DataFrame(mdata)
# print(df)
#
# df.to_csv('MLKL_points.csv')

#*****

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

#*******

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

#********
#
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