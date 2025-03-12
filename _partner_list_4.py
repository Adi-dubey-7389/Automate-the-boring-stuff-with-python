import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
from email import encoders
import pandas as pd
import pymongo
from bson.binary import Binary

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Outsystem"]
partners_collection = db["partners"]

def clean_data(partner_list):
    if not partner_list:
        return set()
    return set(partner.strip() for partner in partner_list)  

def send_email():
    url = 'https://www.outsystems.com/partners/list/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    previous_partner_data = set()
    prev_partner_doc = partners_collection.find_one({"filename": "partner_list_1.xlsx"})
    
    if prev_partner_doc:
        previous_partner_data = clean_data(prev_partner_doc.get("partner_names", []))
        print(f"Previous partner data found: {len(previous_partner_data)} entries.")
    else:
        print("No previous partner data found.")

    partner_data = set()
    web = requests.get(url, headers=headers)
    if web.status_code == 200:
        soup = BeautifulSoup(web.content, 'html.parser')
        page = soup.find_all('div', class_='col-12')

        for first in page:
            name_element = first.find('h6')
            if name_element:
                partner_data.add(name_element.text.strip())

        for page_num in range(2, 42):
            page_url = f'{url}?page={page_num}'
            web_ = requests.get(page_url, headers=headers)
            soup = BeautifulSoup(web_.content, 'html.parser')
            both_ = soup.find_all('div', class_='col-12')
            for both in both_:
                name_element = both.find('h6')
                if name_element:
                    partner_data.add(name_element.text.strip())
    else:
        print(f"Request failed with status code {web.status_code}")

    current_partner_data = clean_data(partner_data)

    new_partners = list(current_partner_data - previous_partner_data)
    removed_partners = list(previous_partner_data - current_partner_data)

    print(f"New Partners Found: {len(new_partners)}")
    print(f"Removed Partners Found: {len(removed_partners)}")

    excel_filename = "partner_list_1.xlsx"
    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        pd.DataFrame(list(current_partner_data), columns=["Partner Names"]).to_excel(writer, sheet_name='Current Partners', index=False)
        pd.DataFrame(new_partners, columns=["New Partner Names"]).to_excel(writer, sheet_name='New Partners', index=False)
        pd.DataFrame(removed_partners, columns=["Removed Partner Names"]).to_excel(writer, sheet_name='Removed Partners', index=False)

    print("File successfully saved locally as partner_list_1.xlsx")

    with open(excel_filename, "rb") as file:
        file_data = Binary(file.read())
        file_document = {
            "filename": "partner_list_1.xlsx",
            "file_data": file_data,
            "partner_names": list(current_partner_data)
        }
        partners_collection.replace_one(
            {"filename": "partner_list_1.xlsx"},
            file_document,
            upsert=True
        )
        print("File successfully saved to MongoDB")

    email_subject = "OutSystems Partners List - Daily Update"
    email_body = "Partners List (attached in Excel file):\n\n"

    if new_partners:
        email_body += f"\nNew Partners: {len(new_partners)} new partners today."
    if removed_partners:
        email_body += f"\nRemoved Partners: {len(removed_partners)} fewer partners today."
    if not new_partners and not removed_partners:
        email_body += "\nNo changes in partner list today."

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
        print("Email sent successfully")

    except Exception as e:
        print(f"Error sending email: {e}")

send_email()
