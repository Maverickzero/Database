#!/usr/bin/python3

import datetime
import peewee

from models import Album, Artist

art = Artist()
alb = Album()
new_artist = art.get_or_create(name = "Newsboys", address = None)
album_one = alb.get_or_create(artist = new_artist,
                              title = "Read All About It",
                              release_date = datetime.date(1988,12,1),
                              publisher = "Refuge",
                              media_type = "CD")
album_one.save()

albums = [{
           "artist": new_artist,
           "title": "Hell is for Wimps",
           "release_date": datetime.date(1990,7,31),
           "publisher": "Sparrow",
           "media_type": "CD"
          },
          {
           "artist": new_artist,
           "title": "Love Liberty Disco",
           "release_date": datetime.date(1999,11,16),
           "publisher": "Sparrow",
           "media_type": "CD"
          },
          {
           "artist": new_artist,
           "title": "Thrive",
           "release_date": datetime.date(2002,3,26),
           "publisher": "Sparrow",
           "media_type": "CD"
          }]

for album in albums:
    a = alb.get_or_create(**album)
    a.save()

bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
for band in bands:
    artist = art.get_or_create(name=band, address=None)
    artist.save()

