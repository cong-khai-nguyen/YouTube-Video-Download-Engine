from tkinter import *
from tkinter import filedialog

# Set up the GUI
screen = Tk()
title = screen.title(
    'YouTube Downloader'
)
canvas = Canvas(screen, width=500, height= 500)
canvas.pack()

# Youtube Logo
logo = PhotoImage(file= 'youtube_logo.png')
# Resize the image
logo = logo.subsample(2,2)

canvas.create_image(250, 80, image = logo)

screen.mainloop()