import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.bestbuy.com/site/asus-rog-zephyrus-m15-15-6-4k-ultra-hd-gaming-laptop-intel-core-i7-16gb-memory-nvidia-geforce-rtx-2060-1tb-ssd-prism-black/6403817.p?skuId=6403817&intl=nosplash'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", {"class": "heading-5 v-fw-regular"}).get_text()
    price = soup.find("div", {"class": "priceView-hero-price priceView-customer-price"}).get_text()
    converted_price = float(price[1:6].replace(',',''))

    if(converted_price < 1600.0):
        send_mail()
        
    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('manjuljain2293@gmail.com', 'onjoebtulmowrlih')

    subject = 'Price fell down!!'
    body = 'Check the link \nhttps://www.bestbuy.com/site/asus-rog-zephyrus-m15-15-6-4k-ultra-hd-gaming-laptop-intel-core-i7-16gb-memory-nvidia-geforce-rtx-2060-1tb-ssd-prism-black/6403817.p?skuId=6403817&intl=nosplash'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'manjuljain2293@gmail.com',
        'manjuljain93@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!!')
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 2)