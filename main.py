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
#                 vieta = columns[0].text.strip()
#             except IndexError:
#                 vieta = ""
#
#             try:
#                 zaidejas = columns[1].text.strip()
#             except IndexError:
#                 zaidejas = ""
#
#             try:
#                 komanda = columns[2].text.strip()
#             except IndexError:
#                 komanda = ""
#
#             try:
#                 rungtynes = columns[3].text.strip()
#             except IndexError:
#                 rungtynes = ""
#
#             try:
#                 suma = columns[4].text.strip()
#             except IndexError:
#                 suma = ""
#
#             data.append({
#                 'Vieta': vieta,
#                 'Zaidejas': zaidejas,
#                 'Komanda': komanda,
#                 'Rungtynes': rungtynes,
#                 'Suma': suma,
#             })
#
#     # Print the scraped data
#     # for entry in data:
#         # print(entry)
#
#     df=pd.DataFrame(data)
#     print(df)
#
# df.to_csv('LKL_points.csv')

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
#                 vieta = columns[0].text.strip()
#             except IndexError:
#                 vieta = ""
#
#             try:
#                 zaidejas = columns[1].text.strip()
#             except IndexError:
#                 zaidejas = ""
#
#             try:
#                 komanda = columns[2].text.strip()
#             except IndexError:
#                 komanda = ""
#
#             try:
#                 rungtynes = columns[3].text.strip()
#             except IndexError:
#                 rungtynes = ""
#
#             try:
#                 suma = columns[4].text.strip()
#             except IndexError:
#                 suma = ""
#
#             data1.append({
#                 'Vieta': vieta,
#                 'Zaidejas': zaidejas,
#                 'Komanda': komanda,
#                 'Rungtynes': rungtynes,
#                 'Suma': suma,
#             })
#
#     df=pd.DataFrame(data1)
#     print(df)
#
# df.to_csv('LKL_rebounds.csv')

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
#                 vieta = columns[0].text.strip()
#             except IndexError:
#                 vieta = ""
#
#             try:
#                 zaidejas = columns[1].text.strip()
#             except IndexError:
#                 zaidejas = ""
#
#             try:
#                 komanda = columns[2].text.strip()
#             except IndexError:
#                 komanda = ""
#
#             try:
#                 rungtynes = columns[3].text.strip()
#             except IndexError:
#                 rungtynes = ""
#
#             try:
#                 suma = columns[4].text.strip()
#             except IndexError:
#                 suma = ""
#
#             data2.append({
#                 'Vieta': vieta,
#                 'Zaidejas': zaidejas,
#                 'Komanda': komanda,
#                 'Rungtynes': rungtynes,
#                 'Suma': suma,
#             })
#
#     df=pd.DataFrame(data2)
#     print(df)
#
# df.to_csv('LKL_assists.csv')

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
#                 vieta = columns[0].text.strip()
#             except IndexError:
#                 vieta = ""
#
#             try:
#                 zaidejas = columns[1].text.strip()
#             except IndexError:
#                 zaidejas = ""
#
#             try:
#                 komanda = columns[2].text.strip()
#             except IndexError:
#                 komanda = ""
#
#             try:
#                 rungtynes = columns[3].text.strip()
#             except IndexError:
#                 rungtynes = ""
#
#             try:
#                 suma = columns[4].text.strip()
#             except IndexError:
#                 suma = ""
#
#             data3.append({
#                 'Vieta': vieta,
#                 'Zaidejas': zaidejas,
#                 'Komanda': komanda,
#                 'Rungtynes': rungtynes,
#                 'Suma': suma,
#             })
#
#     df=pd.DataFrame(data3)
#     print(df)
#
# df.to_csv('LKL_efficiency.csv')