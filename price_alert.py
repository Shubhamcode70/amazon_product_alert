import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

headers = { 'Accept-Language' : "en-GB,en;q=0.8",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'}

response = requests.get("https://www.amazon.in/Sonata-Super-Fibre-Digital-Watch-NH77043PP01/"
                        "dp/B00V6BIF4A/ref=sr_1_39?keywords=sonata+watch&sr=8-39", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price = int(soup.find(class_="a-price-whole").getText())


url = "https://www.amazon.in/Sonata-Super-Fibre-Digital-Watch-NH77043PP01/dp/B00V6BIF4A/ref=sr_1_39?crid=18N13J03DASG8&keywords=sonata+watch&qid=1695812899&sprefix=sonata+watc%2Caps%2C452&sr=8-39"

budget = 600
if price < budget:
    message = "Its Time To Buy Watch!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("xyz", "xyz")
        connection.sendmail(
            from_addr="xyz",
            to_addrs="xyz",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
