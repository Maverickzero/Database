#!/usr/bin/python3
import datetime
import tkinter as tk
from models import Album_Model, Artist_Model, initialize, get_or_create

database = initialize()
if database is None:
    quit()

class Artist(Artist_Model):
    """
    Setting up the database to store the Artist table in
    """
    class Meta:
        database = database

class Album(Album_Model):
    """
    Setting up the database to store the Album table in
    """
    class Meta:
        database = database

db = {
     'Artist': Artist,
     'Album': Album
     }


def add_artist():
    entry = {}
    artist = get_or_create(db=db, mod_type='Artist', dp=True, entry=entry)
    artist.save()


def add_album():
    entry = {}
    artist = get_or_create(db=db, mod_type='Album', dp=True, entry=entry)
    album.save()


main_window = tk.Tk()

# Initializing main window geometry and title
main_window.geometry("350x250")
main_window.resizable(width=False, height=False)
main_window.title('Database application')

# Initializing app text
ask_label = tk.Label(text='What kind of entry do you want to add?')
ask_label.grid()

# Initializing Artist button
button = tk.Button(text='Artist')
button.grid(column=0, row=1)

# Initializing Album button
button = tk.Button(text='Album')
button.grid(column=1, row=1)

# Initializing window form
entry_field = tk.Entry()
entry_field.grid(column=0, row=2)

main_window.mainloop()
