from tkinter import *
from tkinter import filedialog
import pytube
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

# Helper function to get the path from user
def select_path():
    # ask user to select directory path to save
    path = filedialog.askdirectory()
    path_label.config(text=path)

# Helper function to download file
def download_file():
    # Get the YouTube link that the user input
    get_link = link_field.get()
    if get_link == "":
        link_label.config(text = "Please Enter Download Link:")
        return

    # get selected download path
    user_path = path_label.cget("text")
    if user_path == "Select Path For Download" or user_path == "":
        user_path = "Please Select Path For Download"
        path_label.config(text=user_path)

    while user_path == "Please Select Path For Download":
        select_path()
        user_path = path_label.cget("text")

    if user_path == "":
        path_label.config(text="Please Select Path For Download")
        return
    screen.title('Downloading...')
    # Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    # Move file to the selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Donwload Complete! Download Another File...')

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

# Link field and label
link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter Download Link:", font = ('Arial', 15))

# download button
download_btn = Button(screen, text = "Download File", command = download_file)

# Select path to save the file to
path_label = Label(screen, text = "Select Path For Download", font = ('Arial', 15))
select_btn = Button(screen, text = "Select", command=select_path)

# Add link field and label to window
canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)
canvas.create_window(250, 280, window = path_label)
canvas.create_window(250, 330, window = select_btn)
canvas.create_window(250, 360, window = download_btn)

screen.mainloop()