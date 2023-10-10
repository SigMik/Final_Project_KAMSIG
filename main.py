from bs4 import BeautifulSoup
import requests
import pandas as pd

# data=[]
# for p in range(1, 12): #issirenkam pagal pelnomus taskus ir 2022-2023 sezona
#     url = f'https://lkl.lt/get-players-stats?category=points&tab=sums&season_id=32000&additional_filters=0&team_id=-&month=&search_text=&page={p}'
#     response = requests.get(url)
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.prettify())
#
#     table=soup.find("table")
#     if table:
#         rows = table.find_all('tr')
#         for row in rows[1:]:
#             columns = row.find_all('td')
#             try:
#                 place = columns[0].text.strip()
#             except IndexError:
#                 place = ""
#
#             try:
#                 player = columns[1].text.strip()
#             except IndexError:
#                 player = ""
#
#             try:
#                 team = columns[2].text.strip()
#             except IndexError:
#                 team = ""
#
#             try:
#                 games = columns[3].text.strip()
#             except IndexError:
#                 games = ""
#
#             try:
#                 sum = columns[4].text.strip()
#             except IndexError:
#                 sum = ""
#
#             data.append({
#                 'Place': place,
#                 'Player': player,
#                 'Team': team,
#                 'Games': games,
#                 'Sum': sum,
#             })
#
#     df=pd.DataFrame(data)
#     print(df)
#
# df.to_csv('LKL_points.csv')

#*******

# data1=[]
# for p in range(1, 12): #issirenkam pagal rebounds ir 2022-2023 sezona
#     url = f'https://lkl.lt/get-players-stats?category=rebounds&tab=sums&season_id=32000&additional_filters=0&team_id=-&month=&search_text=&page={p}'
#     response = requests.get(url)
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.prettify())
#
#     table=soup.find("table")
#     if table:
#         rows = table.find_all('tr')
#         for row in rows[1:]:
#             columns = row.find_all('td')
#             try:
#                 place = columns[0].text.strip()
#             except IndexError:
#                 place = ""
#
#             try:
#                 player = columns[1].text.strip()
#             except IndexError:
#                 player = ""
#
#             try:
#                 team = columns[2].text.strip()
#             except IndexError:
#                 team = ""
#
#             try:
#                 games = columns[3].text.strip()
#             except IndexError:
#                 games = ""
#
#             try:
#                 sum = columns[4].text.strip()
#             except IndexError:
#                 sum = ""
#
#             data1.append({
#                 'Place': place,
#                 'Player': player,
#                 'Team': team,
#                 'Games': games,
#                 'Sum': sum,
#             })
#
#     df=pd.DataFrame(data1)
#     print(df)
#
# df.to_csv('LKL_rebounds.csv')

#*******
#
# data2=[]
# for p in range(1, 12): #issirenkam pagal assists ir 2022-2023 sezona
#     url = f'https://lkl.lt/get-players-stats?category=assists&tab=sums&season_id=32000&additional_filters=0&team_id=-&month=&search_text=&page={p}'
#     response = requests.get(url)
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.prettify())
#
#     table=soup.find("table")
#     if table:
#         rows = table.find_all('tr')
#         for row in rows[1:]:
#             columns = row.find_all('td')
#             try:
#                 place = columns[0].text.strip()
#             except IndexError:
#                 place = ""
#
#             try:
#                 player = columns[1].text.strip()
#             except IndexError:
#                 player = ""
#
#             try:
#                 team = columns[2].text.strip()
#             except IndexError:
#                 team = ""
#
#             try:
#                 games = columns[3].text.strip()
#             except IndexError:
#                 games = ""
#
#             try:
#                 sum = columns[4].text.strip()
#             except IndexError:
#                 sum = ""
#
#             data2.append({
#                 'Place': place,
#                 'Player': player,
#                 'Team': team,
#                 'Games': games,
#                 'Sum': sum,
#             })
#
#     df=pd.DataFrame(data2)
#     print(df)
#
# df.to_csv('LKL_assists.csv')

#*******

# data3=[]
# for p in range(1, 12): #issirenkam pagal efficiency ir 2022-2023 sezona
#     url = f'https://lkl.lt/get-players-stats?category=efficiency&tab=sums&season_id=32000&additional_filters=0&team_id=-&month=&search_text=&page={p}'
#     response = requests.get(url)
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.prettify())
#
#     table=soup.find("table")
#     if table:
#         rows = table.find_all('tr')
#         for row in rows[1:]:
#             columns = row.find_all('td')
#             try:
#                 place = columns[0].text.strip()
#             except IndexError:
#                 place = ""
#
#             try:
#                 player = columns[1].text.strip()
#             except IndexError:
#                 player = ""
#
#             try:
#                 team = columns[2].text.strip()
#             except IndexError:
#                 team = ""
#
#             try:
#                 games = columns[3].text.strip()
#             except IndexError:
#                 games = ""
#
#             try:
#                 sum = columns[4].text.strip()
#             except IndexError:
#                 sum = ""
#
#             data3.append({
#                 'Place': place,
#                 'Player': player,
#                 'Team': team,
#                 'Games': games,
#                 'Sum': sum,
#             })
#
#     df=pd.DataFrame(data3)
#     print(df)
#
# df.to_csv('LKL_efficiency.csv')