import peewee
import getpass



field_types = {
    'varchar': peewee.CharField,
    'datetime': peewee.DateField
}


def initialize(username=None, password=None, database=None):
    """
    Function used to initialize the database to work in
    """
    username = username if username is not None else input('Username: ')
    password = password if password is not None else getpass.getpass('Password: ')
    database = database if database is not None else input('Database name: ')
    try:
        database = peewee.MySQLDatabase(database, password=password, user=username)
    except peewee.OperationalError:
        print('Failed logging in.')
        database = None
    return database


def fetch_tables(db):
    """
    Returns a list of all tables inside a database.
    """
    return db['mgrDatabase'].get_tables()


def create_models(entries: dict, db, table_name):
    """
    Function used to dinamically create a peewee model of a table
    """
    model_fields = {}

    for key, value in entries.items():
        model_fields[key] = field_types[value['type']](**value['args'])

    class TableModel(peewee.Model):
        """
        ORM model of a fieldless table
        """

        class Meta:
            database = db

    Model = type(table_name, (TableModel,), model_fields)

    return Model

def table_fields(db, table_name):
    """
    Function used to retrieve fields and its types from a table of a database
    """
    fields = {}

    for field in db.get_columns(table_name):
        args = {'null': field.null,
                'primary_key': field.primary_key}
        fields[field.name] = {'type': field.data_type,
                              'args': args}

    return fields

