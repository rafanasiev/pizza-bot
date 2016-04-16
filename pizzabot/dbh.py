# -*- coding: utf-8 -*-


import sqlite3
import os.path

class PizzaBotDB(object):
    ''' PizzaBotDB - it does .... '''
    def __init__(self, dbfile_path):
        if os.path.exists(dbfile_path):
            self.dbfile = dbfile_path
            try:
                self.connection = sqlite3.Connection(self.dbfile)
            except sqlite3.IOError:
                print "ERROR: no such file %s" % (self.dbfile)
        else:
            raise Exception('No such database! Check the path to file')
        self.cursor = self.connection.cursor()


    def select(self, statement):
        ''' select - a common method to do ... '''
        return [row for row in self.cursor.execute(statement)]


    def iud(self, statement):
        ''' iud - '''
        self.cursor.execute(statement)
        self.connection.commit()
