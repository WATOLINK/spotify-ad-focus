import tkinter as tk
from tkinter import messagebox


def button_pressed():
    messagebox.showinfo("Message", "Hey There! I hope you are doing well.")


window = tk.Tk()
window.attributes('-fullscreen', True)
greeting = tk.Button(
    text="work!",
    font=("Arial", 50),
    width=30,
    height=15,
    command = button_pressed
)
greeting.pack()
window.mainloop()
