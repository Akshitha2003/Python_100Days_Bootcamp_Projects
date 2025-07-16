import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib

load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
BUY_PRICE = 100

header = {
    "Accept-Language": "en,en-US;q=0.9,ta;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

product_title = soup.select_one(selector="span#productTitle").getText().split()
product_title = " ".join(product_title)
product_price = float(soup.select_one(selector="span.aok-offscreen").getText().split("$")[1].split()[0])

if product_price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        msg = f"{product_title} is now ${product_price}\n{URL}"
        connection.starttls()
        connection.login(user=os.getenv("GMAIL_ID"), password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr=os.getenv("GMAIL_ID"),
                            to_addrs=os.getenv("GMAIL_ID"),
                            msg=f"Subject:Amazon Price Alert\n\n{msg}".encode("utf-8"))
