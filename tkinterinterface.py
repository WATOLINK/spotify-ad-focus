import tkinter as tk

window = tk.Tk()
window.attributes('-fullscreen', True)
greeting = tk.Button(
    text="you better work",
    font=("Arial", 25),
    width=30,
    height=30

)
greeting.pack()
window.mainloop()
