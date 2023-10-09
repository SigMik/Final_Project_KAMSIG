from bs4 import BeautifulSoup
import requests
import pandas as pd

data=[] #susikuriame sarasa, i kuri desime zaidejus

url = f'https://en.lkl.lt/get-players-stats?category=points&tab=sums&season_id=30527&additional_filters=0&team_id=-&month=&search_text='

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
players = soup.find_all('div', class_='mb-8')
# print(players)


for player in players: #susikuriame kintamuosius
    name= player.find('td', class_='name pr-1').text.strip()
    team = player.find('td', class_='pr-1').text.strip()
    games = player.find('td', class_='pr-1').text.strip()
    sum = player.find('td', class_='pr-1' ).text.strip()
    data.append((name, team, games, sum))

df=pd.DataFrame(data, columns=['Name', 'Team', 'Games', 'Sum'])
print(df)
