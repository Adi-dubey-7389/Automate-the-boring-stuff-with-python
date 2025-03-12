import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
from email import encoders
import pandas as pd
import schedule
import time


def send_email():

    url = 'https://www.outsystems.com/partners/list/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    previous_count = ()
    if os.path.exists("previous_partner_count.txt"):
        with open("previous_partner_count.txt", "r") as f:
            previous_count = int(f.read().strip())

    partner_data = set()

    web = requests.get(url,headers=headers)

    if web.status_code == 200:
        soup = BeautifulSoup(web.content, 'html.parser')
        page = soup.find_all('div', class_='col-12')

        for first in page:
            name_element = first.find('h6')
            if name_element:
                partner_data.add(name_element.text.strip())

        for page_num in range(2, 42):
            page_url = f'{url}?page={page_num}'
            web_ = requests.get(page_url,headers=headers)
            soup = BeautifulSoup(web_.content, 'html.parser')
            both_ = soup.find_all('div', class_='col-12')
            for both in both_:
                name_element = both.find('h6')
                if name_element:
                    partner_data.add(name_element.text.strip())
            

    else:
        print(f"Request failed with status code {response.status_code}")

    partner_data = list(partner_data)
    
    current_count = len(partner_data)
    
    change_message = "There is no changes"
    if current_count != previous_count:
        if current_count > previous_count:
            change_message = f"There are {current_count - previous_count} new partners today."
        else:
            change_message = f"There are {previous_count - current_count} fewer partners today."

    df = pd.DataFrame(partner_data, columns=["Partner Names"])
    excel_filename = "partner_list.xlsx"
    df.to_excel(excel_filename, index=False)

    email_subject = "OutSystems Partners List - Daily Update"
    email_body = f"Partners List (attached in Excel file):\n\n{change_message}"

    sender_email = "aadidubey7389@gmail.com"
    receiver_email = "aditya7389222@gmail.com"
    password = "wqzoemkbgxdfubom"  

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

        with open("previous_partner_count.txt", "w") as f:
            f.write(str(current_count))

    except Exception as e:
        print(f"Error sending email: {e}")


schedule.every().day.at("11:23").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
