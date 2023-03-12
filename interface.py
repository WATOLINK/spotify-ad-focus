from tkinter import *
import pygame

root = Tk()
root.title('Spotify Ad Focus')

root.attributes('-fullscreen', True)

pygame.mixer.init()  # initialise the pygame


def play():
    pygame.mixer.music.load("duck.mp3")
    pygame.mixer.music.play(loops=0)

play_button = Button(
    root,
    text="WORK",
    font=("Helvetica", 70),
    command=play,
    width=30,
    height=15
)
play_button.pack(pady=20)
root.mainloop()