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

# #******
#
# data4=[]
# for p in range(1, 7): #issirenkam pagal tritaskiu metimo taikluma ir 2022-2023 sezona
#     # url = f'https://lkl.lt/get-players-stats?category=3pts_percentage&tab=avg&season_id=32000&additional_filters=0&team_id=-&month=&search_text={p}'
#     url = f'https://lkl.lt/get-players-stats?category=3pts_percentage&tab=avg&season_id=32000&additional_filters=0&team_id=-&month=&search_text={p}'
#     response = requests.get(url)
#     # print(response.status_code)
# #
#     soup = BeautifulSoup(response.text, 'html.parser')
# #     # print(soup.prettify())
# #
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
#                 three_pts_percentage = columns[6].text.strip()
#             except IndexError:
#                 three_pts_percentage = ""
#
#
#             data4.append({
#                 'Place': place,
#                 'Player': player,
#                 'Team': team,
#                 'Three_pts_percentage': three_pts_percentage
#             })
#
#     df=pd.DataFrame(data4)
#     print(df)

# df.to_csv('LKL_3_points_made.csv')

# ******
# issirenkam triju sezonu rezultatus

data2022_2023=[]
for p in range(1, 12): #issirenkam pagal pelnomus taskus ir 2022-2023 sezona
    url = f'https://lkl.lt/get-players-stats?category=points&tab=sums&season_id=32000&additional_filters=0&team_id=-&month=&search_text=&page={p}'
    response = requests.get(url)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    table=soup.find("table")
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            try:
                place = columns[0].text.strip()
            except IndexError:
                place = ""

            try:
                player = columns[1].text.strip()
            except IndexError:
                player = ""

            try:
                team = columns[2].text.strip()
            except IndexError:
                team = ""

            try:
                games = columns[3].text.strip()
            except IndexError:
                games = ""

            try:
                sum = columns[4].text.strip()
            except IndexError:
                sum = ""

            data2022_2023.append({
                'Place': place,
                'Player': player,
                'Team': team,
                'Games': games,
                'Sum': sum,
                'Season': '2022-2023'
            })

df2022_2023=pd.DataFrame(data2022_2023)
# print(df2022_2023)

data2021_2022=[]
for p in range(1, 12): #issirenkam pagal pelnomus taskus ir 2021-2022 sezona
    url = f'https://lkl.lt/get-players-stats?category=points&tab=sums&season_id=30527&additional_filters=0&team_id=-&month=&search_text=&page={p}'
    response = requests.get(url)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    table=soup.find("table")
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            try:
                place = columns[0].text.strip()
            except IndexError:
                place = ""

            try:
                player = columns[1].text.strip()
            except IndexError:
                player = ""

            try:
                team = columns[2].text.strip()
            except IndexError:
                team = ""

            try:
                games = columns[3].text.strip()
            except IndexError:
                games = ""

            try:
                sum = columns[4].text.strip()
            except IndexError:
                sum = ""

            data2021_2022.append({
                'Place': place,
                'Player': player,
                'Team': team,
                'Games': games,
                'Sum': sum,
                'Season': '2021-2022'
            })

df2021_2022=pd.DataFrame(data2021_2022)
# print(df2021_2022)

data2020_2021=[]
for p in range(1, 12): #issirenkam pagal pelnomus taskus ir 2020-2021 sezona
    url = f'https://lkl.lt/get-players-stats?category=points&tab=sums&season_id=28293&additional_filters=0&team_id=-&month=&search_text=&page={p}'
    response = requests.get(url)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    table=soup.find("table")
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            try:
                place = columns[0].text.strip()
            except IndexError:
                place = ""

            try:
                player = columns[1].text.strip()
            except IndexError:
                player = ""

            try:
                team = columns[2].text.strip()
            except IndexError:
                team = ""

            try:
                games = columns[3].text.strip()
            except IndexError:
                games = ""

            try:
                sum = columns[4].text.strip()
            except IndexError:
                sum = ""

            data2020_2021.append({
                'Place': place,
                'Player': player,
                'Team': team,
                'Games': games,
                'Sum': sum,
                'Season': '2020-2021'
            })

df2020_2021=pd.DataFrame(data2020_2021)
# print(df2020_2021)

S3_LKL_points = pd.concat([df2022_2023, df2021_2022, df2020_2021])
print(S3_LKL_points)

S3_LKL_points.to_csv('S3_LKL_points.csv')

