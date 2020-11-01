import pygame 
import tkinter as tk 
from tkinter.filedialog import askdirectory
import os    
musicplayer=tk.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")
directory=askdirectory()
os.chdir(directory)        # Method used to change the current working directory to specified path
songlist=os.listdir()      # Method returns a list containing the names of the entries in the directory given by path
# Method used to display the list items to user
playlist=tk.Listbox(musicplayer,font="Helvetica 12 bold",bg="yellow",selectmode=tk.SINGLE)
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1
pygame.init()              # Initialize pygame modules
pygame.mixer.init()        # Call mixer module of pygame
def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))  # Module of pygame to stream audio and load audio
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
def ExitMusicPlayer():
    pygame.mixer.music.stop() # Method used to stop 
def pause():
    pygame.mixer.music.pause() # Method used to pause
def unpause():
    pygame.mixer.music.unpause() # Method used to unpause
# Declaring and Initializing buttons
Button1=tk.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=play,bg="red",fg="white")
Button2=tk.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="STOP",command=ExitMusicPlayer,bg="purple",fg="white")
Button3=tk.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PAUSE",command=pause,bg="green",fg="white")
Button4=tk.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="blue",fg="white")
var=tk.StringVar()
songtitle=tk.Label(musicplayer,font="Helvetica 12 bold",textvariable=var)
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")
musicplayer.mainloop()

