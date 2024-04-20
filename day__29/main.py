from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

#Generate Password

def generate_password():
    letters=['a','b','c','d','e','f','g','h','i', 'j','k','l','m','n','o']
    numbers=['1','2','3', '4', '5', '6','7','8','9','0']
    symbol=['!', '@','#',"$",'*','&']

    password_l=[choice(letters) for n in range(randint(1,8))]
    password_s = [choice(symbol) for n in range(randint(1, 4))]
    password_n = [choice(numbers) for n in range(randint(1, 4))]
    password_list=password_n+password_l+password_s
    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(titlr="Opps", message="try again")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#labels
website_label=Label(text="Website")
website_label.grid(row=1,column=0)

email_label=Label(text="email")
email_label.grid(row=2, column=0)

password_label=Label(text="password")
email_label.grid(row=2, column=0)

#Entries

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()