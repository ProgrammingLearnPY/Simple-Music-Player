import tkinter
import pygame
import os
from tkinter import filedialog

root = tkinter.Tk()
root.title("ProgrammingLearn")
root.geometry("600x400")
root.resizable(False, False)

pygame.init()
pygame.mixer.init()

def playSong():
    songTrack.config(state='normal')
    songTrack.delete('1.0', tkinter.END)
    songTrack.insert('1.0', playList.get(tkinter.ACTIVE))
    songTrack.config(state='disabled')

    pygame.mixer.music.load(playList.get(tkinter.ACTIVE))
    pygame.mixer.music.play()


def pauseSong():
    pygame.mixer.music.pause()

def unpauseSong():
    pygame.mixer.music.unpause()

def stopSong():
    songTrack.config(state='normal')
    songTrack.delete('1.0', tkinter.END)
    songTrack.config(state='disabled')

    pygame.mixer.music.stop()

def selectFolder():
    folderSelected = filedialog.askdirectory(title='Select Folder')
    if folderSelected:
        playList.delete(0, tkinter.END)
        os.chdir(folderSelected)
        songTracks = os.listdir()
        for i in songTracks:
            if i.endswith(".mp3"):
                playList.insert(tkinter.END, i)

songListFrame = tkinter.LabelFrame(root, bg='grey', bd=1, relief='ridge')
songListFrame.place(x=0, y=0, width=600, height=200)

scroll_y = tkinter.Scrollbar(songListFrame, orient='vertical')
scroll_y.pack(side='right', fill='y')
playList = tkinter.Listbox(songListFrame, selectmode='single', selectbackground='blue', bg='white', fg='black', bd=0, relief='ridge', yscrollcommand=scroll_y.set)
playList.place(x=10, y=10, width=560, height=180)

scroll_y.config(command=playList.yview)


trackFrame = tkinter.LabelFrame(root, bg='grey', bd=1, relief='ridge')
trackFrame.place(x=0, y=200, width=600, height=80)

songTrack = tkinter.Text(trackFrame, bg='white', fg='black', state='disable')
songTrack.place(x=50, y=20, width=500, height=40)

controlFrame = tkinter.LabelFrame(root, bg='grey', bd=1, relief='ridge')
controlFrame.place(x=0, y=280, width=600, height=120)

playButton = tkinter.Button(controlFrame, text='Play', width=10, height=2, bg='white', fg='black', bd=0, command=playSong)
playButton.grid(row=0, column=0, padx=21, pady=35)

pauseButton = tkinter.Button(controlFrame, text='Pause', width=10, height=2, bg='white', fg='black', bd=0, command=pauseSong)
pauseButton.grid(row=0, column=1, padx=21, pady=35)

unpauseButton = tkinter.Button(controlFrame, text='Unpause', width=10, height=2, bg='white', fg='black', bd=0, command=unpauseSong)
unpauseButton.grid(row=0, column=2, padx=21, pady=35)

stopButton = tkinter.Button(controlFrame, text='Stop', width=10, height=2, bg='white', fg='black', bd=0, command=stopSong)
stopButton.grid(row=0, column=3, padx=21, pady=35)

selectButton = tkinter.Button(controlFrame, text='Folder', width=10, height=2, bg='white', fg='black', bd=0, command=selectFolder)
selectButton.grid(row=0, column=4, padx=21, pady=35)

root.mainloop()