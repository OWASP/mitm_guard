import datetime
from . import create_json
class ret_cont_all:
    def __init__(self,cont_all):
        self.c_all = self.return_cont_all(cont_all)
    def return_cont_all(self,cont_all):
        cont_all.setdefault("date", datetime.datetime.now())
        cont_all = (create_json.create_json(cont_all)).ret_json
        return cont_all
