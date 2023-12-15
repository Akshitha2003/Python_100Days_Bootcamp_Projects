from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    chosen_letters = [random.choice(letters) for _ in range(nr_letters)]
    chosen_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    chosen_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = chosen_letters + chosen_symbols + chosen_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {email}\nPassword: {password}"
                                               f"\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    # Reading the old data
                    data = json.load(file)  # type(data) is dictionary
                    # Updating the old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    # Saving the updated data
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", mode="w") as file:
                    # Saving the updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        website_data = data[website_entry.get()]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    except KeyError:  # You can use if-else instead. If there is an easy alternative then don't use exception handling
        messagebox.showerror(title="Error", message=f"No details for the {website_entry.get()} exists")
    else:
        messagebox.showinfo(title=website_entry.get(), message=f"Email: {website_data["email"]}\nPassword: {website_data["password"]}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=49)
email_entry.insert(0, "akshitha@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
