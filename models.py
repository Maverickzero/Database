import peewee
import pymysql

#database = peewee.SqliteDatabase("wee.db")
database = peewee.MySQLDatabase('testDB', password = '@l3ks@ndri@', user = 'jh0wlett')

########################################################################
class Artist(peewee.Model):
    """
    ORM model of the Artist table
    """
    name = peewee.CharField(primary_key = True)
    address = peewee.CharField(null = True)
    def get_or_create(self, name, address):
        try:
            new_artist = Artist.get(Artist.name == name)
        except:
            new_artist = self.create(name = name, address = address)
        return new_artist
    class Meta:
        database = database

########################################################################
class Album(peewee.Model):
    """
    ORM model of album table
    """
    artist = peewee.ForeignKeyField(Artist)
    title = peewee.CharField(primary_key = True)
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()
    def get_or_create(self, artist, title, release_date, publisher, media_type):
        try:
            new_album = Album.get(Album.title == title)
        except:
            new_album =  self.create(artist = artist,
                                     title = title,
                                     release_date = release_date,
                                     publisher = publisher,
                                     media_type = media_type)
        return new_album
    class Meta:
        database = database

try:
    Artist.create_table()
except (peewee.OperationalError, peewee.InternalError):
    print("Artist table already exists!")

try:
    Album.create_table()
except (peewee.OperationalError, peewee.InternalError):
    print("Album table already exists!")

