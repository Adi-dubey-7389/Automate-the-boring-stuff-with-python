import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.outsystems.com/partners/list/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

partner_data = set()
web = requests.get(url,headers=headers)

if web.status_code == 200:
    soup = BeautifulSoup(web.content,'html.parser')

    both_ = soup.find_all('div',class_ = 'col-12')


    for both in both_:

        name = both.find('h6')

        if name:
            partner_data.add(name.text.strip())

    for page_num in range(2, 42):

        page_url = f'{url}?page={page_num}'

        soup_ = BeautifulSoup(requests.get(page_url,headers=headers).content,'html.parser')

        both__ = soup_.find_all('div',class_ = 'col-12')

        for bot in both__:

            name = bot.find('h6')

            if name:
                partner_data.add(name.text.strip())

    partner_data = list(partner_data)
    df = pd.DataFrame(partner_data, columns=['Partner Name'])
    df.to_csv('partners.csv', index=False)

else:
    print(f"Request failed with status code {response.status_code}")

        

        
    
