import requests
from bs4 import BeautifulSoup
import pandas as pa

url = 'https://www.aksuniversity.ac.in/courses/All-Programs'

web = requests.get(url)

soup = BeautifulSoup(web.content,'html.parser')

both_ = soup.find_all('div',class_ = 'card h-100')

courses_data = []

for both in both_:

    name = both.find('h3').text

    des = both.find('p').text

    courses_data.append({'Name':name,'Description':des})

for page_num in range(1, 5):

    page_url = f'{url}?page={page_num}'

    soup_ = BeautifulSoup(requests.get(page_url).content,'html.parser')

    both__ = soup_.find_all('div',class_ = 'card h-100')

    for bot in both__:

        name = bot.find('h3').text

        des = bot.find('p').text

        courses_data.append({'Name':name,'Description':des})

df = pa.DataFrame(courses_data)

df.to_excel('courses.xlsx')

        

        
    
    











