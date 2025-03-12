import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

url = 'https://www.outsystems.com/partners/list/'

previous_count = 0
if os.path.exists("previous_partner_count.txt"):
    with open("previous_partner_count.txt", "r") as f:
        previous_count = int(f.read().strip())

partner_data = []

web = requests.get(url)
soup = BeautifulSoup(web.content,'html.parser')
page = soup.find_all('div',class_ = 'col-12')

for first in page:
    name_element = first.find('h6')
    if name_element:
        partner_data.append(name_element.text.strip())

for page_num in range(2, 42):
    page_url = f'{url}?page={page_num}'
    web = requests.get(page_url)
    soup = BeautifulSoup(web.content, 'html.parser')
    both_ = soup.find_all('div', class_='col-12')

    for both in both_:
        name_element = both.find('h6')
        if name_element:
            partner_data.append(name_element.text.strip())

current_count = len(partner_data)

change_message = ""
if current_count != previous_count:
    if current_count > previous_count:
        change_message = f"There are {current_count - previous_count} new partners today."
    else:
        change_message = f"There are {previous_count - current_count} fewer partners today."

email_subject = "OutSystems Partners List - Daily Update"
email_body = f"Partners List:\n\n" + "\n".join(partner_data) + "\n\n{change_message}"

sender_email = "aadidubey7389@gmail.com"
receiver_email = "aditya7389222@gmail.com"
password = "wqzoemkbgxdfubom"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))

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
