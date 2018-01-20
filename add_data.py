#!/usr/bin/python3

import datetime
import peewee
import pdb
from models import Album_Model, Artist_Model, initialize


database = initialize()
if database is None:
    quit()

class Artist(Artist_Model):
    """
    Setting up the database to store the Artist tables in
    """
    class Meta:
        database = database

class Album(Album_Model):
    """
    Setting up the database to store the Album tables in
    """
    artist = peewee.ForeignKeyField(Artist)
    class Meta:
        database = database

art = Artist()
alb = Album()
artist = art.get_or_create(Artist)
artist.save()
album = alb.get_or_create(database, Artist)
album.save()

