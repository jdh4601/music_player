import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
# canvas.resizable(True, True)
canvas.config(bg='black')
# canvas.pack()
# img = PhotoImage(file="music.png")
# canvas.create_image(20, 20, image=img)
rootpath = "/users/jayden/Desktop/music"
pattern = "*.mp3"
mixer.init()

prev_img = tk.PhotoImage(file="button/prev_img.png")
stop_img = tk.PhotoImage(file="button/stop_img.png")
play_img = tk.PhotoImage(file="button/play_img.png")
pause_img = tk.PhotoImage(file="button/pause_img.png")
next_img = tk.PhotoImage(file="button/next_img.png")

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100)
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', background='black', fg='orange', bd=5)
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')


prevButton = tk.Button(canvas, text="Prev", image=prev_img, background="black", borderwidth=0)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg="black", borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg="black", borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Stop", image=pause_img, bg="black", borderwidth=0)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg="black", borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

listBox.insert(0, "Coding1")
listBox.insert(1, "Coding2")
listBox.insert(2, "Coding3")
listBox.insert(3, "Coding4")

canvas.mainloop()
