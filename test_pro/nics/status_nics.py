import netifaces
from ..get_services import save_in_file
import json
import hashlib
class status_nics:
    def __init__(self, all_nics, cont_all):
        self.all_nics = self.status_inters(all_nics, cont_all)
    def get_class_name(self):
        return __class__.__name__
    def status_inters(self, all_nics, cont_all):
        dict_all_status_inters = {}
        all_status_inters = {}
        all_status_int = {}
        all_status = {}
        dict_all_status = {}
        inic = 0
        for m in range(len(all_nics)):
            check_inter = netifaces.ifaddresses(all_nics[m])
            if len(check_inter) == 1:
                all_status_inters.setdefault(all_nics[m], "down")
                dict_all_status_inters.setdefault(all_nics[m], "down")
            elif (len(check_inter) >= 1) and (netifaces.ifaddresses(all_nics[m])[netifaces.AF_INET][0]['addr'] == "127.0.0.1") :
                all_status_inters.setdefault(all_nics[m], "up")
                dict_all_status_inters.setdefault(all_nics[m], "up")
            else:
                all_status_inters.setdefault(all_nics[m], "up")
                dict_all_status_inters.setdefault(all_nics[m], "up")
            inic += 1
            all_status.setdefault(inic ,all_status_inters)
            all_status_inters = {}
        save_in_file.save_in_file(cont_all,self.get_class_name(),all_status)
        return dict_all_status_inters
