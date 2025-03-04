import requests
from bs4 import BeautifulSoup
import gspread as gs
import pandas as pa
import gspread_dataframe as gd

url = 'https://www.aksuniversity.ac.in/courses/All-Programs'

web = requests.get(url)

soup = BeautifulSoup(web.content,'html.parser')

both_ = soup.find_all('div',class_ = 'card h-100')

courses_data = []

for both in both_:

    name = both.find('h3').text

    des = both.find('p').text

    courses_data.append({'Name':name,'Description':des})

for page_num in range(1,5):

    page_url = f'{url}?page={page_num}'

    soup_ = BeautifulSoup(requests.get(page_url).content,'html.parser')

    both__ = soup_.find_all('div',class_ = 'card h-100')

    for bot in both__:

        name = bot.find('h3').text

        des = bot.find('p').text

        courses_data.append({'Name':name,'Description':des})

gc = gs.service_account(filename="C:\\python\\aks-courses-0bf37ec46b11.json")

work_sheet = gc.open_by_key('1M9QA_MZsqv4RISRrt4AJ2TgphzQ0Png890zN2jtqH0w')

current_sheet = work_sheet.worksheet('Sheet1')

df = pa.DataFrame(courses_data)

gd.set_with_dataframe(current_sheet,df)







        

        
    
    











