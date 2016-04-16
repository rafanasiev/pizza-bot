import sqlite3
import os.path

class PizzaBotDB(object):

    def __init__(self, dbfile_path):
        if os.path.exists(dbfile_path):
            self.dbfile = dbfile_path
            self.connection = sqlite3.Connection(self.dbfile)
        else:
            raise Exception('No such database! Check the path to file')
        self.cursor = self.connection.cursor()


    def select(self, statement):
        return [row for row in self.cursor.execute(statement)]


    def iud(self, statement):
        self.cursor.execute(statement)
        self.connection.commit()
