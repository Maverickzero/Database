from datetime import datetime
import tkinter as tk

from copy import copy
from functools import partial
from models import ArtistModel, AlbumModel, fetch_fields, fetch_tables, get_or_create, initialize


LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)


class DBApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.database = None
        self.title('Database modification app')

        self.frames = {}

    def show_frame(self, name):

        frame = self.frames[name]
        frame.tkraise()

    def add_frame(self, container, entries: list=None, name: str='Start Page'):

        if name == 'Login Page':
            frame = LoginPage(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
        elif name == 'Start Page':
            frame = StartPage(container, self, entries)
            frame.grid(row=0, column=0, sticky="nsew")
        else:
            frame = EntryPage(container, self, entries=entries, name=name)
            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[name] = frame

    def startup(self):
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.add_frame(container=self.container, name='Login Page')
        self.show_frame('Login Page')

    def main_page(self, database):
        db = database

        class Artist(ArtistModel):
            """
            Setting up the database to store the Artist table in
            """
            class Meta:
                database = db


        class Album(AlbumModel):
            """
            Setting up the database to store the Album table in
            """
            class Meta:
                database = db

        db = {
            'artist': Artist,
            'album': Album,
            'mgrDatabase': database
        }

        for child in self.frames['Login Page'].winfo_children():
            child.destroy()
        del self.frames['Login Page']

        self.database = db

        tables = fetch_tables(db)

        for table in tables:
            entries = fetch_fields(db, table)
            self.add_frame(container=self.container, entries=entries, name=table)

        self.add_frame(container=self.container, entries=tables)
        self.show_frame('Start Page')


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Fill in your credentials and database name:", font=LARGE_FONT)
        label.grid(column=0, row=0)

        self.entries = ['username', 'password', 'database']
        self.labels = {}
        self.forms = {}

        row = 1
        for entry in self.entries:
            self.labels[entry] = tk.Label(self, text=entry, font=SMALL_FONT)
            self.labels[entry].grid(column=0, row=row)

            self.forms[entry] = tk.Entry(self)
            self.forms[entry].grid(column=1, row=row)

            if entry == 'password':
                self.forms[entry].config(show='*')
            row += 1

        self.button = tk.Button(self, text='Login',
                                command=partial(self.login, controller))
        self.button.grid(column=0, row=row)

    def login(self, controller):
        """
        Get credentials from forms after button being pressed and try to login
        """
        credentials = {}
        for entry in self.entries:
            credentials[entry] = self.forms[entry].get()
            self.forms[entry].delete(0, 'end')

        database = initialize(**credentials)

        if database is None:
            self.login(controller)
        else:
            controller.main_page(database)


class StartPage(tk.Frame):

    def __init__(self, parent, controller, tables: list):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Which entry do you want to add?", font=LARGE_FONT)
        label.grid(column=0, row=0)

        self.buttons = {}

        row = 1
        for table in tables:
            self.buttons[table] = tk.Button(self, text=table,
                                            command=partial(controller.show_frame, table))
            self.buttons[table].grid(column=0, row=row)
            row += 1


class EntryPage(tk.Frame):

    def __init__(self, parent, controller, entries: list, name: str):
        tk.Frame.__init__(self, parent)
        self.name = name

        self.label = tk.Label(self, text="Fill in the entries bellow:", font=LARGE_FONT)
        self.label.grid(column=0, row=0)

        self.labels = {}
        self.forms = {}

        self.entries = entries

        row = 1
        for entry in entries:
            self.labels[entry] = tk.Label(self, text=entry, font=SMALL_FONT)
            self.labels[entry].grid(column=0, row=row)

            self.forms[entry] = tk.Entry(self)
            self.forms[entry].grid(column=1, row=row)
            row += 1

        self.button = tk.Button(self, text="Add", command=partial(self.add_entry, controller))
        self.button.grid(column=0, row=row)

    def add_entry(self, controller):

        entry_dict = {}
        for entry in self.entries:
            entry_dict[entry] = self.forms[entry].get()
            if entry == 'release_date':
                entry_dict[entry] = datetime.strptime(entry_dict[entry], '%Y-%m-%d')
            self.forms[entry].delete(0, 'end')

        get_or_create(db=controller.database, mod_type=self.name, entry=entry_dict, dp=True)
        controller.show_frame('Start Page')


if __name__ == "__main__":
    app = DBApp()
    app.startup()
    app.mainloop()

