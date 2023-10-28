
# Import libraries
from tkinter import *
from tkinter import messagebox
from password_gen import password_gen

# Parameters
DEFAULT_EMAIL = "thiago.strava.correa@gmail.com"
PASSWORD_FILE = "password_file.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password_button():
    suggested_password = password_gen()
    input_password.delete(0, "end")
    input_password.insert(0, suggested_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = input_website.get()
    user = input_user.get()
    password = input_password.get()
    
    new_line = " | ".join([website,
                    user,
                    password]) + "\n"
    
    if (len(website) == 0) or (len(user) == 0) or (len(password) == 0):
        messagebox.showwarning(title="Empty field", message="Please fill out all fields!")
    else:
        is_ok = messagebox.askokcancel(
            title = input_website.get(),
            message = f"These are the details entered:\nE-mail: {user}\nPassword: {password}\n Is it ok to save?")

        if is_ok:
            with open(PASSWORD_FILE, "a") as file:
                file.write(new_line)

            input_website.delete(0, "end")
            input_password.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# Lock canvas
canvas = Canvas(width = 200, height = 200)
pomodoro_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = pomodoro_image)
canvas.grid(column=0, row=0, columnspan=3)

# Label: "Website:"
label_01 = Label(text="Website:", pady=2)
label_01.grid(column=0, row=1)

#Input website
input_website = Entry(width=52)
input_website.focus()
input_website.grid(column=1, row=1, columnspan=2)

# Label: "Email/Username:"
label_02 = Label(text="Email/Username:", pady=2)
label_02.grid(column=0, row=2)

#Input user
input_user = Entry(width=52)
input_user.insert(0, DEFAULT_EMAIL)
input_user.grid(column=1, row=2, columnspan=2)

# Label: "Password:"
label_03 = Label(text="Password:", pady=2)
label_03.grid(column=0, row=3)

#Input password
input_password = Entry(width=32)
input_password.grid(column=1, row=3)

# Button: "Generate Password"
button_gen = Button(text = "Generate Password", width = 15, pady=2, command=gen_password_button)
button_gen.grid(column=2, row=3)

# Button: "Add"
button_add = Button(text = "Add", width = 45, pady=2, command = save_password)
button_add.grid(column=1, row=4, columnspan=2)

# Main loop
window.mainloop()
