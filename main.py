
from tkinter import *
import tkinter as tk
import pygame
import os
import random
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

folder = "music"
is_paused = False
index = 0
song_list = []
def load_songs():
    current = 0
    global song_list

    if not os.path.isdir(folder):
        print(f"Folder '{folder} not found")
        return
    music_files = [file for file in os.listdir(folder)if file.lower().endswith((".mp3", ".wav", ".flac"))]
    if not music_files: 
        print("No music files found!")
    for index, song in enumerate(music_files, start =0):
        song_list.append(music_files[index])
    return song_list   
 
def play_music(songs):
    global index
    song = songs[index]
    file_path = os.path.join(folder, song)

    if not os.path.exists(file_path):
        print("File not found")
        return

    pygame.mixer.music.load(file_path)   
    pygame.mixer.music.play()

    print(f"\nNow playing: {song}")


def pause_music():
    global is_paused
    if is_paused == False:
        pygame.mixer.music.pause()
        is_paused = True
        print("Paused")

    elif is_paused == True:
        pygame.mixer.music.unpause()
        is_paused = False
        print("Unpaused")


def next_music(songs):
    limit = len(songs)
    
    pygame.mixer.music.stop()
    global index
    index = index + 1
    if index > limit:
        index = limit - 1 
    current_song_print.config(text=songs[index])

    song = songs[index]
    file_path = os.path.join(folder, song)

    if not os.path.exists(file_path):
        print("File not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    

def prev_music(songs):
    limit = len(songs)
    pygame.mixer.music.stop()
    global index

    index = index - 1
    current_song_print.config(text=songs[index])
    if index < 0:
        index = 0
    song = songs[index]    
    file_path = os.path.join(folder, song)

    if not os.path.exists(file_path):
        print("File not found")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def song_click(i):
    global song_list
    global index
    index = i
    current_song_print.config(text=song_list[index])

    song = song_list[index]    
    file_path = os.path.join(folder, song)

    pygame.mixer.music.load(file_path)   
    pygame.mixer.music.play()

    print(f"\nNow playing: {song}")
        

def load_window():
    global current_song_print
    songs = load_songs()
    root = Tk()
    root.title("Music Player")
    root.geometry("500x300")

    menubar = Menu(root)
    root.config(menu=menubar)

    organise_menu = Menu(menubar, tearoff=False)
    organise_menu.add_command(label='Select Folder')
    menubar.add_cascade(label='Organise', menu=organise_menu)

    songs_frame = Frame(root, width=150, height=300, bg="grey")
    songs_frame.pack(padx=0, pady=0, side=LEFT, fill=Y)
    current_song_print = Label(songs_frame,text=songs[index],bg="White", fg="black")
    current_song_print.pack(padx=5, pady=5)
    for i, song in enumerate(songs):
        song_print = Button(songs_frame,text=song,bg="blue", fg="blue",command=lambda i=i:song_click(i)) #When this function is created, take the current value of i and store it as a default value inside the function.
        song_print.pack(padx=0, pady=0,)

    bottomlist = Listbox(root, bg="black", fg="grey", width=100, height=15)
    bottomlist.pack()


    play_btn_image = PhotoImage(file="Utils/play.png")
    pause_btn_image = PhotoImage(file="Utils/pause.png")
    next_btn_image = PhotoImage(file="Utils/next.png")
    prev_btn_image = PhotoImage(file="Utils/previous.png")

    control_frame = Frame(root)
    control_frame.pack()

    play_btn = Button(control_frame, image=play_btn_image, borderwidth=0,command=play_music(songs))
    pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0,command=pause_music)
    next_btn = Button(control_frame, image=next_btn_image, borderwidth=0,command=lambda: next_music(songs))
    prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0,command=lambda: prev_music(songs))

    play_btn.grid(row=0, column=1, padx=7, pady=10)
    pause_btn.grid(row=0, column=2, padx=7, pady=10)
    next_btn.grid(row=0, column=3, padx=7, pady=10)
    prev_btn.grid(row=0, column=0, padx=7, pady=10)

    root.mainloop() 

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Error", e)
        return
    load_window()


if __name__ == "__main__":
    main()

