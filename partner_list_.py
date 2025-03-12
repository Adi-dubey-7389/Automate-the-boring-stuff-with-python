import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import pandas as pd
import schedule
import time
import pymongo
from email import encoders
import urllib.parse
import logging
from dotenv import load_dotenv

sender_email = "aadidubey7389@gmail.com"
receiver_email = "aditya7389222@gmail.com"
password = ('wqzoemkbgxdfubom')  

username = urllib.parse.quote(os.getenv('Adity_Dubey'))
password = urllib.parse.quote(os.getenv('@Adi7389'))

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.f9x9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
db = client['Web_scrapping']  
collection = db['partners']  

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    
def send_email():
    url = 'https://www.outsystems.com/partners/list/'

    previous_partners = set()
    stored_partners = collection.find()
    for partner in stored_partners:
        previous_partners.add(partner['name'])

    partner_data = set()

    try:
        web = requests.get(url,headers=headers)
        web.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return

    soup = BeautifulSoup(web.content, 'html.parser')
    page = soup.find_all('div', class_='col-12')

    for first in page:
        name_element = first.find('h6')
        if name_element:
            partner_data.add(name_element.text.strip())

    for page_num in range(2, 42):  
        page_url = f'{url}?page={page_num}'
        try:
            web_ = requests.get(page_url,headers=headers)
            web_.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request error on page {page_num}: {e}")
            continue

        soup = BeautifulSoup(web_.content, 'html.parser')
        both_ = soup.find_all('div', class_='col-12')
        for both in both_:
            name_element = both.find('h6')
            if name_element:
                partner_data.add(name_element.text.strip())

        

    added_partners = partner_data - previous_partners
    removed_partners = previous_partners - partner_data

    change_message = "There are no changes in the partner list."
    if added_partners or removed_partners:
        change_message = f"Changes detected:\n\n"

        if added_partners:
            change_message += f"New partners added:\n" + "\n".join(added_partners) + "\n\n"

        if removed_partners:
            change_message += f"Partners removed:\n" + "\n".join(removed_partners) + "\n\n"

    collection.delete_many({})

    for partner in partner_data:
        collection.insert_one({"name": partner})

    df = pd.DataFrame(list(partner_data), columns=["Partner Names"])
    excel_filename = "partner_list_.xlsx"
    df.to_excel(excel_filename, index=False)

    email_subject = "OutSystems Partners List - Daily Update"
    email_body = f"Partners List (attached in Excel file):\n\n{change_message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'plain'))

    with open(excel_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={excel_filename}")
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

schedule.every().day.at("12:20").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
