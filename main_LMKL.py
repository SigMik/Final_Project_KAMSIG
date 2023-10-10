from bs4 import BeautifulSoup
import requests
import pandas as pd

# wdata=[]
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
#             vieta = columns[0].text.strip()
#         except IndexError:
#             vieta = ""
#
#         try:
#             zaideja = columns[1].text.strip()
#         except IndexError:
#             zaideja = ""
#
#         try:
#             PTS = columns[2].text.strip()
#         except IndexError:
#             PTS = ""
#
#         try:
#             komanda = columns[3].text.strip()
#         except IndexError:
#             komanda = ""
#
#         try:
#             GM = columns[4].text.strip()
#         except IndexError:
#             GM = ""
#
#         try:
#             PTS_min = columns[5].text.strip()
#         except IndexError:
#             PTS_min = ""
#
#         try:
#             PTS_max = columns[6].text.strip()
#         except IndexError:
#             PTS_max = ""
#
#         wdata.append({
#             'Vieta': vieta,
#             'Zaideja': zaideja,
#             'PTS': PTS,
#             'Komanda': komanda,
#             'GM': GM,
#             'PTS_min': PTS_min,
#             'PTS_max': PTS_max
#         })
#
#
# df=pd.DataFrame(wdata)
# print(df)
#
# df.to_csv('MLKL_points.csv')

# wdata1=[]
# #issirenkam pagal atkovotus kamuolius ir 2022-2023 sezona
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=reb&sort=total&games_type=all'
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
#             vieta = columns[0].text.strip()
#         except IndexError:
#             vieta = ""
#
#         try:
#             zaideja = columns[1].text.strip()
#         except IndexError:
#             zaideja = ""
#
#         try:
#             REB = columns[2].text.strip()
#         except IndexError:
#             REB = ""
#
#         try:
#             komanda = columns[3].text.strip()
#         except IndexError:
#             komanda = ""
#
#         try:
#             GM = columns[4].text.strip()
#         except IndexError:
#             GM = ""
#
#         try:
#             REB_min = columns[5].text.strip()
#         except IndexError:
#             REB_min = ""
#
#         try:
#             REB_max = columns[6].text.strip()
#         except IndexError:
#             REB_max = ""
#
#         wdata1.append({
#             'Vieta': vieta,
#             'Zaideja': zaideja,
#             'REB': REB,
#             'Komanda': komanda,
#             'GM': GM,
#             'REB_min': REB_min,
#             'REB_max': REB_max
#         })
#
#
# df=pd.DataFrame(wdata1)
# print(df)
#
# df.to_csv('MLKL_rebounds.csv')

# wdata2=[]
# #issirenkam pagal rezultatyvius perdavimus ir 2022-2023 sezona
#
# url = 'https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason=2022&fmonth=0&stage=0&fpos=as&sort=total&games_type=all'
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
#             vieta = columns[0].text.strip()
#         except IndexError:
#             vieta = ""
#
#         try:
#             zaideja = columns[1].text.strip()
#         except IndexError:
#             zaideja = ""
#
#         try:
#             AS = columns[2].text.strip()
#         except IndexError:
#             AS = ""
#
#         try:
#             komanda = columns[3].text.strip()
#         except IndexError:
#             komanda = ""
#
#         try:
#             GM = columns[4].text.strip()
#         except IndexError:
#             GM = ""
#
#         try:
#             AS_min = columns[5].text.strip()
#         except IndexError:
#             AS_min = ""
#
#         try:
#             AS_max = columns[6].text.strip()
#         except IndexError:
#             AS_max = ""
#
#         wdata2.append({
#             'Vieta': vieta,
#             'Zaideja': zaideja,
#             'AS': AS,
#             'Komanda': komanda,
#             'GM': GM,
#             'AS_min': AS_min,
#             'AS_max': AS_max
#         })
#
#
# df=pd.DataFrame(wdata2)
# print(df)
#
# df.to_csv('MLKL_assists.csv')

# wdata3=[]
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
#             EFF = columns[2].text.strip()
#         except IndexError:
#             EFF = ""
#
#         try:
#             team = columns[3].text.strip()
#         except IndexError:
#             team = ""
#
#         try:
#             GM = columns[4].text.strip()
#         except IndexError:
#             GM = ""
#
#         try:
#             EFF_min = columns[5].text.strip()
#         except IndexError:
#             EFF_min = ""
#
#         try:
#             EFF_max = columns[6].text.strip()
#         except IndexError:
#             EFF_max = ""
#
#         wdata3.append({
#             'Place': place,
#             'Player': player,
#             'EFF': EFF,
#             'Team': team,
#             'GM': GM,
#             'EFF_min': EFF_min,
#             'EFF_max': EFF_max
#         })
#
#
# df=pd.DataFrame(wdata3)
# print(df)
#
# df.to_csv('MLKL_efficiency.csv')