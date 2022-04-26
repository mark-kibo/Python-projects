import os
import tkinter as tk
import pytube
from tkinter import filedialog, messagebox
from pytube import YouTube, Playlist
import threading
import urllib


window = tk.Tk()
window.title("y o u t u b e  d o w n l o a d e r")
window.resizable(False, False)
window.geometry(f"500x500")
window.config(background="orange")

link = tk.StringVar()
download_path = tk.StringVar()


def save_file():
    download_path.set(filedialog.askdirectory(initialdir="./"))


def downloading():

    yt = YouTube(str(link.get()))
    title = yt.title
    videos = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

    tk.Label(window, text="downloading......").pack(pady=10)
    videos.download(output_path=download_path.get())
    messagebox.showinfo(title="download", message="download complete")
    tk.Label(window, text=f"""{title}
        has been downloaded.
        access it in the follwing path {download_path.get()} 
        """).pack(pady=10)


label1 = tk.Label(window, text="E N T E R  L I N K", fg="white", bg="black", border=False)

label1.pack(pady=10)

entry1 = tk.Entry(window, textvariable=link)
entry1.pack(pady=10)

label2 = tk.Label(window, text="d o w n l o a d p a t h", fg="black")
label2.pack(pady=10)

button1 = tk.Button(window, text="BROWSE", bg="blue", command=save_file)
button1.pack(pady=10)

entry2 = tk.Entry(window, textvariable=download_path)
entry2.pack(pady=10)

button2 = tk.Button(window, text="D o w n l o a d", bg="green", fg="black",
                    command=downloading)
button2.pack(pady=10)

window.mainloop()
