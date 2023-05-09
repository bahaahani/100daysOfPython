from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label( text="Website: ")
website.grid(column=0,row=1)

email = Label( text="Emale: ")
email.grid(column=0,row=2)

passwd = Label( text="Password: ")
passwd.grid(column=0,row=3)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
emale_entry = Entry(width=35)
emale_entry.insert(0,"Blainefire00@gmail.com")
emale_entry.grid(row=2,column=1, columnspan=2)
pwd_entry = Entry(width=21)
pwd_entry.grid(row=3,column=1)


generatepwd= Button(text="Generate Password")
generatepwd.grid(row=3,column=2)

addbutton = Button(text="Add", width=36)
addbutton.grid(row=4, column=1, columnspan=2)

window.mainloop()