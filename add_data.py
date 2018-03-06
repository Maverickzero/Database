#!/usr/bin/python3
from window_manager import DBApp
from models import AlbumModel, ArtistModel, initialize

database = initialize()
if database is None:
    quit()


class Artist(ArtistModel):
    """
    Setting up the database to store the Artist table in
    """
    class Meta:
        database = database


class Album(AlbumModel):
    """
    Setting up the database to store the Album table in
    """
    class Meta:
        database = database


db = {
     'artist': Artist,
     'album': Album,
     'mgrDatabase': database
     }

if __name__ == "__main__":
    app = DBApp()
    app.startup(db=db)
    app.mainloop()
