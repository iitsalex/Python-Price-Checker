import requests  # for web download
from bs4 import BeautifulSoup  # for parsing
import time  # delay requests
import smtplib  # email when changes detected
from email.mime.multipart import MIMEMultipart # handling subject, body, etc.
from email.mime.text import MIMEText # handling text of message
from datetime import datetime
while True:
    url = "https://novelkeys.xyz/collections/switches/products/novelkeys-x-kailh-box-pinks"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "lxml")

    reg_price = soup.find("span", {"class": "price-item price-item--regular"}).text.strip()
    sale_price = soup.find("span", {"class", "price-item price-item--sale"}).text.strip()

    if reg_price == sale_price:
        time.sleep(60)
        continue
    else:
        print('regular price: ' + reg_price)
        print('sale price: ' + sale_price)
        now = datetime.now()
        message = ('As of ' + str(now) + '\nregular price: ' + reg_price + "\nsale_price "  + sale_price)
        msg = MIMEMultipart()

        msg['From'] = 'fioratheworst@gmail.com'
        msg['To'] = "iitsalex@hotmail.com"
        msg['Subject'] = "NovelKeys Box Pinks Price Adjustment!"

        msg.attach(MIMEText(message,'plain'))

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("fioratheworst@gmail.com", "fake-password")

        # send the email
        server.send_message(msg)
        # disconnect from the server
        server.quit()

        break
