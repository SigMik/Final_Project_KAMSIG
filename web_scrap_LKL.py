from bs4 import BeautifulSoup
import requests
import pandas as pd

# ## LKL WEB SCRAPING BY POINTS
# ## creating empty list for data storing
# data=[]
# ## scraping LKL data by total points category from chosen website
# ## using for loop to scrape the data over each URL page
# for p in range(1, 12):
#     url = (f'https://lkl.lt/get-players-stats?category=points&tab=sums&season_id=32000&additional_filters=0&'
#            f'team_id=-&month=&search_text=&page={p}')
# ##checking the URL response
#     response = requests.get(url)
#     # print(response.status_code)
# ## getting needed data from URL as table and indicating analysis method
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.prettify())
#
# ## extracting the data from the required table columns
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
# ## appending data list from scraped table
#             data.append({
#                 'Place': place,
#                 'Player': player,
#                 'Team': team,
#                 'Games': games,
#                 'Sum': sum,
#             })
# ## creating DataFrame to store the collected data
#     df=pd.DataFrame(data)
#     print(df)
#
# ## exporting LKL points data to csv file
# # df.to_csv('LKL_points.csv')
#
# ## LKL WEB SCRAPING BY EFFICIENCY
# ## creating emppty list for data storing
# data3=[]
# ## scraping LKL data by efficiency ratio category from chosen website
# ## using for loop to scrape the data over each URL page
# for p in range(1, 12):
#     url = (f'https://lkl.lt/get-players-stats?category=efficiency&tab=sums&season_id=32000&additional_filters=0&team'
#            f'_id=-&month=&search_text=&page={p}')
# ## checking the URL response
#     response = requests.get(url)
#     # print(response.status_code)
# ## getting needed data from URLs as table indicating analysis method
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.prettify())
# ## extracting the data from the required table columns
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
# ## creating DataFrame to store the collected data
#     df=pd.DataFrame(data3)
#     print(df)

## exporting LKL efficiency data to csv file
# df.to_csv('LKL_efficiency.csv')

### LKL WEB SCRAPING BY AVERAGE POINTS EARNED BY TEAMS AND THREE SEASONS

## creating emppty list for data storing
# data2022_2023=[]
#
# ## scraping LKL data by teams, average points and 2022-2023 season
# url ='https://lkl.lt/get-teams-stats?category=points&tab=avg&season_id=32000'
#
# ## checking the URL response
# response = requests.get(url)
# # print(response.status_code)
#
# ## getting needed data from URLs as table indicating analysis method
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# ## extracting the data from the required table columns
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
# ## creating DataFrame to store the collected data
# df2022_2023=pd.DataFrame(data2022_2023)
# # print(df2022_2023)
#
# ## creating emppty list for data storing
# data2021_2022=[]
#
# ### scraping LKL data by teams, average points and 2021-2022 season
# url ='https://lkl.lt/get-teams-stats?category=points&tab=avg&season_id=30527'
#
# ## checking the URL response
# response = requests.get(url)
# # print(response.status_code)
#
# ## getting needed data from URLs as table indicating analysis method
# soup = BeautifulSoup(response.text, 'html.parser')
#  # print(soup.prettify())
#
# ## extracting the data from the required table columns
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
# ## creating DataFrame to store the collected data
# df2021_2022=pd.DataFrame(data2021_2022)
# # print(df2021_2022)
#
# ## creating emppty list for data storing
# data2020_2021=[]
#
# ## scraping LKL data by teams, average points and 2021-2022 season
# url ='https://lkl.lt/get-teams-stats?category=points&tab=avg&season_id=28293'
#
# ## checking the URL response
# response = requests.get(url)
# # print(response.status_code)
#
# ## getting needed data from URLs as table indicating analysis method
# soup = BeautifulSoup(response.text, 'html.parser')
#  # print(soup.prettify())
#
# ## extracting the data from the required table columns
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
# ## creating DataFrame to store the collected data
# df2020_2021=pd.DataFrame(data2020_2021)
# # print(df2020_2021)
#
# ## using concat function to combine the collected data into one DataFrame
# BS3_LKL_points = pd.concat([df2022_2023, df2021_2022, df2020_2021])
# print(BS3_LKL_points)

### exporting LKL data from three seasons into one csv file
# BS3_LKL_points.to_csv('BS3_LKL_points.csv')
