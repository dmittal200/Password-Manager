from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

#password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 2))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_E.insert(0, password)
    pyperclip.copy(password)


#Save data
def save():
    website = website_E.get()
    email = email_E.get()
    password = password_E.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure to fill all the details.")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details you entered:\n Email: {email}\n Password: {password}")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f'{website} : {email} : {password} \n')
                website_E.delete(0,END)
                password_E.delete(0,END)



canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_img)
canvas.grid(column=1,row=0)

#Labels
website_L = Label(text="Website:")
website_L.grid(column=0,row=1)
email_L = Label(text="Email/Username:")
email_L.grid(column=0,row=3)
password_L = Label(text="Password:")
password_L.grid(column=0,row=5)

#Entries
website_E = Entry(width=51)
website_E.grid(column=1, row=1,columnspan=2)
website_E.focus()
email_E = Entry(width=51)
email_E.grid(column=1, row=3,columnspan=2)
email_E.insert(0,"ddevansh82@gmail.com")
password_E = Entry(width=32)
password_E.grid(column=1, row=5)

#Buttons
generate_B = Button(text="Generate Password",highlightthickness=0, command=generate_password)
generate_B.grid(column=2,row=5)
add_B = Button(text="Add",width=44,highlightthickness=0, command=save)
add_B.grid(column=1,row=7,columnspan=2)


window.mainloop()
