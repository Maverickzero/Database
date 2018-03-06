import peewee
import pymysql
import getpass
from datetime import datetime


def get_or_create(db: dict, mod_type: str, get: bool = False, dp: bool = False, entry: dict = None):
    instance = None
    if not dp:
        args = db[mod_type].fetch_entry(db, get)
    else:
        args = entry
    try:
        instance = db[mod_type].create(**args)
    except peewee.IntegrityError:
        if mod_type == 'Artist':
            instance = db[mod_type].get(db[mod_type].name == args['name'])
        elif mod_type == 'Album':
            instance = db[mod_type].get(db[mod_type].artist == args['title'])
    return instance


def initialize():
    """
    Function used to initialize the database to work in
    """
#    username = input('Username: ')
#    password = getpass.getpass('Password: ')
#    dbname = input('Database name: ')
    username = 'jh0wlett'
    password = '@l3ks@ndri@'
    dbname = 'testDB'
    try:
        database = peewee.MySQLDatabase(dbname, password=password, user=username)
        database.connect()
    except peewee.OperationalError:
        print('Failed logging in.')
        database = None
    return database


def fetch_fields(db, mod_type):
    fields = []
    for key, value in db[mod_type].__dict__.items():
        if isinstance(value, peewee.FieldDescriptor):
            fields.append(key)
    return fields


def fetch_tables(db):
    return db['mgrDatabase'].get_tables()


class ArtistModel(peewee.Model):
    """
    ORM model of the Artist table
    """
    name = peewee.CharField(primary_key = True)
    address = peewee.CharField(null = True)

    def fetch_entry(db, get = None):
        if get is None:
            artist = {
                     'name': input('Name of the artist: '),
                     'address': input('Address of the artist: ')
                     }
        else:
            artist = {'name': input('Name of the artist: ')}
        return artist


class AlbumModel(peewee.Model):
    """
    ORM model of album table
    """
    title = peewee.CharField(primary_key = True)
    release_date = peewee.DateTimeField(null = True)
    publisher = peewee.CharField(null = True)
    media_type = peewee.CharField(null = True)
    artist = peewee.ForeignKeyField(ArtistModel, null = True)

    def fetch_entry(db, get = None):
        if get is None:
            album = {
                    'artist': get_or_create(db, 'Artist', get = True),
                    'title': input('Name of title: '),
                    'publisher': input('Name of publisher: '),
                    'media_type': input('Media type: '),
                    'release_date': input('Date of release (1970-01-01): ')
                    }
        else:
            album = {'title': input('Name of title: ')}
        return album

