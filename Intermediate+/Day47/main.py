import requests
from bs4 import BeautifulSoup
import lxml
url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

r=requests.get(url=url, headers={"Accept-Language":"en-US,en;q=0.9,ar-BH;q=0.8,ar;q=0.7","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


# part 2 
import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
#optional
#     with smtplib.SMTP("blainefire00@gmail.com", port=587) as connection:
#         connection.starttls()
#         result = connection.login("blainefire00@gmail.com", "BlaineFire00")
#         connection.sendmail(
#             from_addr="",
#             to_addrs="YOUR_EMAIL",
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
#         )