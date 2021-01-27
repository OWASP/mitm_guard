import netifaces
class available_nic:
    def __init__(self, status_nics, all_nics, cont_all_local):
        self.available_n = self.avail_nic(status_nics, all_nics, cont_all_local)
    def get_class_name(self):
        return __class__.__name__
    def avail_nic(self, status_nics, all_nics, cont_all_local):
        list_all_key = []
        list_all_val = []
        list_new_nics = []
        dict_available_nics = {}
        ii = 1
        for jjj in range(len(status_nics)):
            list_all_key.append(list(status_nics.keys())[jjj])
            list_all_val.append(list(status_nics.values())[jjj])
        for m in range(len(status_nics)):
            if (list_all_val[m] == 'down') or ((list_all_val[m] == 'up') and \
               (netifaces.ifaddresses(all_nics[m])[netifaces.AF_INET][0]['addr'] == "127.0.0.1")):
                pass
            else:
                list_new_nics.append(list(status_nics.keys())[m])
                dict_available_nics.setdefault(ii,list(status_nics.keys())[m])
                ii = ii+1
        cont_all_local.setdefault(self.get_class_name(),dict_available_nics)
        return list_new_nics
