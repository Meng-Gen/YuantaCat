#-*- coding: utf-8 -*-

from yuantacat.database.postgres_database import PostgresDatabase

class Database():
    def __init__(self):
        self.impl = PostgresDatabase("dbname='stockcat' user='stockcat' host='localhost' password='stockcat'")

    def store(self, feed):
        return self.impl.store(feed)

    def get(self, operation, param):
        return self.impl.get(operation, param)
