
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


def CreateWidgets():

    linkLabel = Label(root, text="Link video : ", bg="skyblue")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)
    root.linkText = Entry(root, width=40)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)
    destinationLabel = Label(root, text="Save Dir : ", bg="skyblue")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)
    root.destinationText = Entry(root, width=25)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)
    browseButton = Button(root, text="Browse", command=Browse, width=10)
    browseButton.grid(row=2, column=2, pady=5, padx=5)
    dwldButton = Button(root, text="Download", command=Download, width=20)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)

def Browse():
    root.destinationDIR = filedialog.askdirectory(initialdir = "/root/Documents/youtube/")
    root.destinationText.insert('1', root.destinationDIR)


def Download():

    getVideo = YouTube(root.linkText.get())
    videoStream = getVideo.streams.first()
    videoStream.download(root.destinationDIR)

    messagebox.showinfo("Success", "Video Downloaded and save in : \n"+root.destinationDIR)

root = tk.Tk()
root.geometry("530x120")
root.title("YouTube Downloader")
root.resizable(False, False)
root.config(background="skyblue")

CreateWidgets()

root.mainloop()
