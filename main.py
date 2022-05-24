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

# Link field
link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter Download Link: ")

# Add widgets to window
canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)

screen.mainloop()