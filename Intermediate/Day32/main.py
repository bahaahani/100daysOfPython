import smtplib
import random
my_emale = "blainefire00@gmail.com"
with open ("./Intermediate/Day32/quotes.txt") as quotes:
    quote_list = quotes.read()
muneera = "202009254@stu.uob.edu.bh"
quote_list = quote_list.split("\n")
quote = random.choice(quote_list)
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_emale, password="zyhuriuzrbjrrntn")
for i in range(10):
    quote = random.choice(quote_list)
    connection.sendmail(
        from_addr=my_emale,
        to_addrs=muneera,
        msg=f"Subject:Hewwo Meow Pls take 496 its not retarded\n\nHewwo sent from python day 32\n{quote}."
    )
connection.close()