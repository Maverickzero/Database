import tkinter as tk

from functools import partial
from datetime import datetime
from db_utils import initialize, table_fields, create_models


LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)


class DBApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.database = None
        self.title('Database modification app')

        self.frames = {}

    def show_frame(self, name):
        """
        Shows frame from controller's frame set.
        args:
        name = name of the frame to be shown
        """
        frame = self.frames[name]
        frame.tkraise()

    def add_frame(self, container, entries: list=None, name: str='Start Page'):
        """
        Creates a new frame of one of the known types, and adds them to the
        controller frame set.
        args:
        container = tk.Frame container to pass to pages
        entries = entries used by page to create forms and fields
        name = name of the page
        """
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
        """
        Startup the app by creating a frame container and a login frame,
        and showing the login frame.
        """
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.add_frame(container=self.container, name='Login Page')
        self.show_frame('Login Page')

    def main_page(self, db):
        """
        Creates all table frames and start page.
        args:
        db = connected peewee database object
        """

        for child in self.frames['Login Page'].winfo_children():
            child.destroy()
        del self.frames['Login Page']

        tables = db.get_tables()

        manager = {'mgrDatabase': db}

        for table in tables:
            entries = table_fields(db, table)
            manager[table] = create_models(entries, db, table)
            self.add_frame(container=self.container, entries=entries.keys(), name=table)

        self.database = manager

        self.add_frame(container=self.container, entries=tables)
        self.show_frame('Start Page')

    def exit_protocol(self):
        """
        Elegantly closes database before exisiting app.
        """
        if self.database is not None:
            self.database['mgrDatabase'].close()
        self.destroy()


class BasePage(tk.Frame):
    """
    Base Page class with needed variables for different
    applications.
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.labels = {}
        self.forms = {}
        self.buttons = {}


class LoginPage(BasePage):
    """
    Login page that asks for credentials before
    connecting with database.
    """
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent)
        self.labels['mgrTitle'] = tk.Label(self, text="Fill in your credentials and database name:",
                                           font=LARGE_FONT)
        self.labels['mgrTitle'].grid(column=0, row=0)

        self.entries = ['username', 'password', 'database']

        row = 1
        for entry in self.entries:
            self.labels[entry] = tk.Label(self, text=entry, font=SMALL_FONT)
            self.labels[entry].grid(column=0, row=row)

            self.forms[entry] = tk.Entry(self)
            self.forms[entry].grid(column=1, row=row)

            if entry == 'password':
                self.forms[entry].config(show='*')
            row += 1

        self.buttons['login'] = tk.Button(self, text='Login',
                                command=partial(self.login, controller))
        self.buttons['login'].grid(column=0, row=row)

    def login(self, controller):
        """
        Get credentials from forms after button being pressed and try to login
        args:
        controller = app controller needed to show next page
        """
        credentials = {}
        for entry in self.entries:
            credentials[entry] = self.forms[entry].get()
            self.forms[entry].delete(0, 'end')

        database = initialize(**credentials)
        database.connect()

        if database is None:
            self.login(controller)
        else:
            controller.main_page(database)


class StartPage(BasePage):
    """
    Start page containing buttons of each table in
    the database to be able to update them.
    """
    def __init__(self, parent, controller, tables: list):
        BasePage.__init__(self, parent)
        self.labels['mgrTitle'] = tk.Label(self, text="Which entry do you want to add?",
                                           font=LARGE_FONT)
        self.labels['mgrTitle'].grid(column=0, row=0)

        row = 1
        for table in tables:
            self.buttons[table] = tk.Button(self, text=table,
                                            command=partial(controller.show_frame, table))
            self.buttons[table].grid(column=0, row=row)
            row += 1


class EntryPage(BasePage):
    """
    Page for adding an entry to the database.
    """
    def __init__(self, parent, controller, entries: list, name: str):
        BasePage.__init__(self, parent)
        self.name = name

        self.labels['mgrTitle'] = tk.Label(self, text="Fill in the entries bellow:",
                                           font=LARGE_FONT)
        self.labels['mgrTitle'].grid(column=0, row=0)

        self.entries = entries

        row = 1
        for entry in entries:
            self.labels[entry] = tk.Label(self, text=entry, font=SMALL_FONT)
            self.labels[entry].grid(column=0, row=row)

            self.forms[entry] = tk.Entry(self)
            self.forms[entry].grid(column=1, row=row)
            row += 1

        self.buttons['add'] = tk.Button(self, text="Add",
                                        command=partial(self.add_entry, controller))
        self.buttons['add'].grid(column=0, row=row)

    def add_entry(self, controller):
        """
        Tries to create an entry in the database after gathering
        strings in the field forms.
        args:
        controller = app controller needed to show next page
        """
        entry_dict = {}
        for entry in self.entries:
            entry_dict[entry] = self.forms[entry].get()
            if entry == 'release_date':
                entry_dict[entry] = datetime.strptime(entry_dict[entry], '%Y-%m-%d')
            self.forms[entry].delete(0, 'end')

        try:
            controller.database[self.name].get_or_create(**entry_dict)
        except peewee.IntegrityError:
            """
            To do: handle integrity checks when trying to create an entry in a table
            that is referencing an inexistent entry in another
            """
            pass

        controller.show_frame('Start Page')


if __name__ == "__main__":
    app = DBApp()
    app.protocol("WM_DELETE_WINDOW", app.exit_protocol)
    app.startup()
    app.mainloop()

