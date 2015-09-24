#-*- coding: utf-8 -*-

from yuantacat.database.postgres_get_command import PostgresGetCommnad
from yuantacat.database.postgres_store_command import PostgresStoreCommand

class PostgresDatabase():
    def __init__(self, connection_string):
        self.store_command = PostgresStoreCommand(connection_string)
        self.get_command = PostgresGetCommnad(connection_string)

    def store(self, feed):
        return self.store_command.store(feed)

    def get(self, operation, param):
        return self.get_command.get(operation, param)
