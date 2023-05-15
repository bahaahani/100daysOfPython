from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    pwd_entry.delete(0,END)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
                'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
                    'T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*','(',')','_','+'] 

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    passwd_list = password_letters + password_symbols + password_numbers
    random.shuffle(passwd_list)
    password = "".join(passwd_list)
    pwd_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) ==0 or len(pwd_entry.get()) ==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: {emale_entry.get()}\nPassword: {pwd_entry.get()}\nIs it ok to save?")
        if is_ok:
            with open("data.txt",'a') as data_file:
                data_file.write(f"{website_entry.get()} | {emale_entry.get()} | {pwd_entry.get()}\n")
                website_entry.delete(0,END)
                pwd_entry.delete(0,END)

          
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
# logo =PhotoImage(file="logo.png")
canvas.create_image(100, 100)#image=logo)
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
pwd_entry = Entry(width=35)
pwd_entry.grid(row=3,column=1, columnspan=2)#hmm2


generatepwd= Button(text="Generate", command=generate_password)
generatepwd.grid(row=4,column=2)

addbutton = Button(text="Add", width=36, command=save)
addbutton.grid(row=4, column=0, columnspan=2)

window.mainloop()