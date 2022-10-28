from importlib.resources import path
from select import select
from tkinter import *
from tkinter import filedialog
from turtle import title
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#Functions
def select_path():
    #Select Directory on PC
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading!')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    #move file 
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete!')






screen = Tk()
title = screen.title('Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()


#logo
logo_img = PhotoImage(file='Youtube-Logo.png')

#resize
logo_img = logo_img.subsample(35, 35)

canvas.create_image(250, 20, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Paste the Download Link", font=('Sans Serif', 20) )



#Path(Directory)
path_label = Label(screen, text="Select Path for file", font=('Sans Serif', 12))
select_btn = Button(screen, text="Select", command=select_path)

#Add to Window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 310, window=select_btn)

#Widgets 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)



#Download-Button
download_btn = Button(screen, text="Download", command=download_file)
canvas.create_window(250, 390, window=download_btn)



screen.mainloop()

