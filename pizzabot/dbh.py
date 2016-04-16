# -*- coding: utf-8 -*-


import sqlite3
import os.path
import json

class PizzaBotDB(object):
    ''' PizzaBotDB - it does .... '''
    def __init__(self, dbfile_path='/home/vagrant/db/TestDB.db'):
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

    def insert(self, argument):
        result_str = json.dumps(argument)
        self.cursor.execute("INSERT INTO Service (service_info) VALUES (?);", (result_str,))
        self.connection.commit()


    def iud(self, statement, field):
        ''' iud - '''
        self.cursor.execute(statement, field)
        self.connection.commit()
