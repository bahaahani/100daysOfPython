import smtplib
import random
my_emale = "blainefire00@gmail.com"
with open ("./Intermediate/Day32/quotes.txt") as quotes:
    quote_list = quotes.read()

quote_list = quote_list.split("\n")
quote = random.choice(quote_list)
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_emale, password="zyhuriuzrbjrrntn")
connection.sendmail(
    from_addr=my_emale,
    to_addrs=my_emale,
    msg=f"Subject:Hewwo\n\nHewwo {quote}."
)
connection.close()