from pymongo import MongoClient
class db_conn:
    def __init__(self):
        self.db_server = self.connections()
    def connections(self):
        conn = MongoClient('192.168.1.105',
                              username='main_db',
                              password='1368-box',
                              authSource='alma_db',
                              port = 27017)
        return conn
