from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pytube
from pytube import YouTube

def save():
    button_resoultion1.config(state=NORMAL)
    button_resoultion2.config(state=NORMAL)
    button_resoultion3.config(state=NORMAL)
    global Folderdir
    filename = filedialog.askdirectory()
    Folderdir = filename
    print(filename)

def quality1():
    try:
        video = Link_entry.get()
        yt = YouTube(video)
        download_label.config(text='   VIDEO DOWNLOADED -    ')
        name = yt.title
        video_title.config(text=name)
        video_resolution.config(text="|  QUALITY - 144p  |")
        download_144 = yt.streams.get_by_itag('17')
        download_144.download(Folderdir)
        messagebox.showinfo(title="DOWNLOAD COMPLETE",message="Your Video has been downloaded")


    except:
        messagebox.showerror(title="ERROR",message="Please Enter a valid link")

def quality2():
    try:
        video = Link_entry.get()
        yt = YouTube(video)
        download_label.config(text='   VIDEO DOWNLOADED -    ')
        name = yt.title
        video_title.config(text=name)
        video_resolution.config(text="|  QUALITY - 360p  |")
        download_360 = yt.streams.get_by_itag('18')
        download_360.download(Folderdir)
        messagebox.showinfo(title="DOWNLOAD COMPLETE", message="Your Video has been downloaded")
    except:
        messagebox.showerror(title="ERROR", message="Please Enter a valid link")


def quality3():
    try:
        video = Link_entry.get()
        yt = YouTube(video)
        download_label.config(text='   VIDEO DOWNLOADED -    ')
        name = yt.title
        video_title.config(text=name)
        video_resolution.config(text="|  QUALITY - 720p  |")
        download_720 = yt.streams.get_by_itag('22')
        download_720.download(Folderdir)
        messagebox.showinfo(title="DOWNLOAD COMPLETE", message="Your Video has been downloaded")
    except:
        messagebox.showerror(title="ERROR", message="Please Enter a valid link")



def song_location():
    button_resoultion1_.config(state=NORMAL)
    button_resoultion2_.config(state=NORMAL)
    global Folderdir_
    filename = filedialog.askdirectory()
    Folderdir_ = filename
    print(filename)

def quality48():
    try:
        audio = Link_entry_.get()
        yt_ = YouTube(audio)
        download_label_.config(text='   SONG DOWNLOADED -    ')
        name_ = yt_.title
        video_title_.config(text=name_)
        video_resolution_.config(text="|  QUALITY - 48kbps  |")
        download_48 = yt_.streams.filter(progressive=False).get_by_itag('139')
        download_48.download(Folderdir_)
        messagebox.showinfo(title="DOWNLOAD COMPLETE", message="Your Song has been downloaded")
    except:
        messagebox.showerror(title="ERROR", message="Please Enter a valid link")



def quality128():
    try:
        audio = Link_entry_.get()
        yt_ = YouTube(audio)
        download_label_.config(text='   SONG DOWNLOADED -    ')
        name_ = yt_.title
        video_title_.config(text=name_)
        video_resolution_.config(text="|  QUALITY - 48kbps  |")
        download_128 = yt_.streams.filter(progressive=False).get_by_itag('140')
        download_128.download(Folderdir_)
    except:
        messagebox.showerror(title="ERROR", message="Please Enter a valid link")


window = Tk()
window.geometry("400x600")
window.config(background='#363636')
window.title("YOUTUBE DOWNLOADER")
photo = PhotoImage(file='Youtubepic.jpg')
photo_ = PhotoImage(file='SeekPng.com_youtube-logo-button-png_9085589 (2).png') #This file may not be uploaded in the directory
window.iconphoto(True,photo_)


notebook = ttk.Notebook(window)
notebook.pack(expand=True,fill='both')
video_tab = Frame(notebook,bg='#363636')
song_tab = Frame(notebook,bg='#363636')
notebook.add(video_tab,text="DOWNLOAD VIDEOS")
notebook.add(song_tab,text="DOWNLOAD SONGS")

image_frame = Frame(video_tab,width=400,bg='#555555')  #video tab logo
photo_label = Label(image_frame,image=photo,width=400,bg='#555555')
image_frame.grid(row=0,column=0,columnspan=2)
photo_label.grid(row=0,column=0,columnspan=2)

empty_label = Label(video_tab,bg='#363636',text="DOWNLOAD YOUTUBE VIDEOS",font=('Rubik',10),fg='white')
Link_label = Label(video_tab,
                   text="Copy Link : ",
                   bg='#363636',fg='white')
Link_entry = Entry(video_tab,width=45)
button_frame = Frame(video_tab)

Folderdir = StringVar()
Folderdir.set("Save")
lowquality = IntVar()
lowquality.set("144p")
path_locationlabel = Label(video_tab,
                           text="| PATH LOCATION |",bg='#363636',fg='white')
location_button = Button(video_tab,
                         text="CHOOSE PATH",padx=10,bg='#555555',activebackground='#363636',activeforeground='white',command=save,textvariable=Folderdir)
resolution = Label(video_tab,bg='#363636',text='| Select the resolution |',fg='white')
button_resoultion1 = Button(video_tab,
                            text="144p", padx=10,bg='#555555',activebackground='#363636',activeforeground='white',command=quality1,state=DISABLED,textvariable=lowquality)
button_resoultion2 = Button(video_tab,
                       text="360p",padx=10,bg='#555555',activebackground='#363636',activeforeground='white',command=quality2,state=DISABLED)
button_resoultion3 = Button(video_tab,
                       text="720p",padx=10, bg='#555555',activebackground='#363636',activeforeground='white', command=quality3,state=DISABLED)


empty_1 = Label(video_tab,bg='#363636')

download_label = Label(video_tab,bg='#363636',fg='#555555',font=('Rubik',10,'underline'))
video_title = Label(video_tab,bg='#363636',fg='#555555')
video_resolution = Label(video_tab,bg='#363636',fg='#555555')

completed_label = Label(video_tab,bg='#363636',fg='#555555')


empty_label.grid(row=1,column=0,columnspan=2)
Link_label.grid(row=2,column=0)
Link_entry.grid(row=2,column=1)
path_locationlabel.grid(row=3,column=0,columnspan=2)
location_button.grid(row=4,column=0,columnspan=2)
resolution.grid(row=5,column=0,columnspan=2)
button_frame.grid(row=6,column=0,columnspan=2)
button_resoultion1.grid(row=6,column=0,columnspan=2)
button_resoultion2.grid(row=7,column=0,columnspan=2)
button_resoultion3.grid(row=8,column=0,columnspan=2)
empty_1.grid(row=9,column=0)
download_label.grid(row=10,column=0,columnspan=2)
video_title.grid(row=11,column=0,columnspan=2)
video_resolution.grid(row=12,column=0,columnspan=2)
completed_label.grid(row=13,column=0,columnspan=2)






image_frame_ = Frame(song_tab,width=400,bg='#555555')  #Song tab logo
photo_label_ = Label(image_frame_,image=photo,width=400,bg='#555555')
image_frame_.grid(row=0,column=0,columnspan=2)
photo_label_.grid(row=1,column=0,columnspan=2)


empty_label_ = Label(song_tab,bg='#363636',text="DOWNLOAD YOUTUBE VIDEO SONGS",font=('Rubik',10),fg='white')
Link_label_ = Label(song_tab,
                   text="Copy Link : ",
                   bg='#363636',fg='white')
Link_entry_ = Entry(song_tab,width=45)
button_frame_ = Frame(song_tab)

Folderdir_ = StringVar()
Folderdir_.set("Save")
path_locationlabel_ = Label(song_tab,text="| PATH LOCATION |",bg='#363636',fg='white')
location_button_ = Button(song_tab,text="CHOOSE PATH",padx=10,bg='#555555',activebackground='#363636',activeforeground='white',command=song_location,textvariable=Folderdir_)

resolution_ = Label(song_tab,text="| Select the resolution |",bg='#363636',fg='white')

button_resoultion1_ = Button(song_tab,
                       text="48kbps",padx=13,bg='#555555',activebackground='#363636',activeforeground='white',state=DISABLED,command=quality48)
button_resoultion2_ = Button(song_tab,
                       text="128kbps",padx=10,bg='#555555',activebackground='#363636',activeforeground='white',state=DISABLED,command=quality128)

empty_1_ = Label(song_tab,bg='#363636')

download_label_ = Label(song_tab,bg='#363636',fg='#555555',font=('Rubik',10,'underline'))
video_title_ = Label(song_tab,bg='#363636',fg='#555555')
video_resolution_ = Label(song_tab,bg='#363636',fg='#555555')

#completed_label_ = Label(video_tab,bg='#363636',fg='#555555')


empty_label_.grid(row=1,column=0,columnspan=2)
Link_label_.grid(row=2,column=0)
Link_entry_.grid(row=2,column=1)
path_locationlabel_.grid(row=3,column=0,columnspan=2)
location_button_.grid(row=4,column=0,columnspan=2)
resolution_.grid(row=5,column=0,columnspan=2)
button_frame_.grid(row=6,column=0,columnspan=2)
button_resoultion1_.grid(row=6,column=0,columnspan=2)
button_resoultion2_.grid(row=7,column=0,columnspan=2)
empty_1_.grid(row=8,column=0)
download_label_.grid(row=9,column=0,columnspan=2)
video_title_.grid(row=10,column=0,columnspan=2)
video_resolution_.grid(row=11,column=0,columnspan=2)
#completed_label_.grid(row=12,column=0,columnspan=2)



window.mainloop()