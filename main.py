from bs4 import BeautifulSoup
import requests


url = 'https://lkl.lt/statistika'

response = requests.get(url)

print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
#imame visus elementus is bloko, kuriame yra zaideju info
zaideju_info = soup.find_all('div', class_='mb-8')
print(zaideju_info)
