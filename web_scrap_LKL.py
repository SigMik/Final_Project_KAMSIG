from bs4 import BeautifulSoup
import requests
import pandas as pd

# scraping data from we site
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

# ******
# issirenkam triju sezonu rezultatus

# data2022_2023=[]
#
# url ='https://lkl.lt/get-teams-stats?category=points&tab=avg&season_id=32000'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#  # print(soup.prettify())
#
# table=soup.find("table")
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             team = columns[1].text.strip()
#         except IndexError:
#             team = ""
#
#         try:
#             avg = columns[4].text.strip()
#         except IndexError:
#             avg = ""
#
#         data2022_2023.append({
#             'Team': team,
#             'Avg': avg,
#             'Season': '2022-2023'
#          })
#
# df2022_2023=pd.DataFrame(data2022_2023)
# # print(df2022_2023)
#
#
# data2021_2022=[]
#
# url ='https://lkl.lt/get-teams-stats?category=points&tab=avg&season_id=30527'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#  # print(soup.prettify())
#
# table=soup.find("table")
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             team = columns[1].text.strip()
#         except IndexError:
#             team = ""
#
#         try:
#             avg = columns[4].text.strip()
#         except IndexError:
#             avg = ""
#
#         data2021_2022.append({
#             'Team': team,
#             'Avg': avg,
#             'Season': '2021-2022'
#          })
#
# df2021_2022=pd.DataFrame(data2021_2022)
# # print(df2021_2022)
#
#
# data2020_2021=[]
#
# url ='https://lkl.lt/get-teams-stats?category=points&tab=avg&season_id=28293'
# response = requests.get(url)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#  # print(soup.prettify())
#
# table=soup.find("table")
# if table:
#     rows = table.find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         try:
#             team = columns[1].text.strip()
#         except IndexError:
#             team = ""
#
#         try:
#             avg = columns[4].text.strip()
#         except IndexError:
#             avg = ""
#
#         data2020_2021.append({
#             'Team': team,
#             'Avg': avg,
#             'Season': '2020-2021'
#          })
#
# df2020_2021=pd.DataFrame(data2020_2021)
# # print(df2020_2021)
#
# BS3_LKL_points = pd.concat([df2022_2023, df2021_2022, df2020_2021])
# print(BS3_LKL_points)

# BS3_LKL_points.to_csv('BS3_LKL_points.csv')
