
from tkinter import *
from tkinter import messagebox
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.delete(0,END)
    password_entry.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(email)==0 or len(password==0):
        messagebox.showwarning(title="Not filled properly", message="PLease fill up all the details")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail: {email}\nPassword: {password}\n is it ok to save?")
        if is_ok:
            with open("datafile.txt", "a") as datafile:
                datafile.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=50,bg="white")

# CANVAS STARTS HERE
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# WEB SITE LAYOUT
website_text = Label(text="Website", font=(FONT_NAME, 10))
website_text.grid(column=0, row=1)
website_entry = Entry(width=43)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# EMAIL LAYOUT
email_text = Label(text="Email/Username:", font=(FONT_NAME, 10))
email_text.grid(column=0, row=2)
email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)

# PASSWORD LAYOUT
password_text = Label(text="Password :", font=(FONT_NAME, 10))
password_text.grid(column=0, row=3)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# PASSWORD BUTTON LAYOUT
create_pass = Button(text="Generate Password", command=password)
create_pass.grid(row=3, column=2)

# ADD BUTTON LAYOUT
add_btn = Button(text="Generate Password", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
