#!/usr/bin/python3

import datetime
import peewee
import pdb
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

artist = get_or_create(Artist, db, 'Artist')
artist.save()
album = get_or_create(Album, db, 'Album')
album.save()

