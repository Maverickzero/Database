import peewee
import pymysql
import getpass
import datetime


def initialize():
    """
    Function used to initialize the database to work in
    """
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    dbname = input('Database name: ')
    try:
        database = peewee.MySQLDatabase(dbname, password = password, user = username)
    except peewee.OperationalError:
        print('Try again')
        database = None
    return database


class Artist_Model(peewee.Model):
    """
    ORM model of the Artist table
    """
    name = peewee.CharField(primary_key = True)
    address = peewee.CharField(null = True)

    def get_or_create(self, Artist):
        """
        Function used to create an entry in the artist table
        """
        name = input('Name of the artist: ')
        address = input('Address of the artist: ')
        try:
            new_artist = Artist.get(Artist.name == name)
        except:
            new_artist = self.create(name = name, address = address)
        return new_artist


class Album_Model(peewee.Model):
    """
    ORM model of album table
    """
    title = peewee.CharField(primary_key = True)
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()

    def get_or_create(self, database, Artist):
        """
        Function used to create an entry in the album table
        """
        artist = input('Name of the artist: ')
        artist = Artist.get(Artist.name == artist)
        title = input('Name of the title: ')
        release_date = input('Date of release of album (format is 1970-01-01): ')
        release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        publisher = input('Name of the publisher: ')
        media_type = input('Type of media: ')
        try:
            new_album = Album.get(Album.title == title)
        except:
            new_album =  self.create(artist = artist,
                                     title = title,
                                     release_date = release_date,
                                     publisher = publisher,
                                     media_type = media_type)
        return new_album

