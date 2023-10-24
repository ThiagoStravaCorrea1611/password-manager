
# Import libraries
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

# Lock canvas
canvas = Canvas(width = 200, height = 200)
pomodoro_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = pomodoro_image)
canvas.pack()

# Main loop
window.mainloop()
