from ..get_services import save_in_file
from ..cryptography import hash_log
import hashlib
import json
class arp_cache:
    def __init__(self, cont_all):
        self.get_arp = self.get_arp_cache(cont_all)
    def get_class_name(self):
        return __class__.__name__
    def get_arp_cache(self, cont_all):
        with open("/proc/net/arp") as f:
            content = f.readlines()
            del content[0]
            arp_dic = {}
            vvv = {}
            content_new = None
            iii = 1
            for aaa in range(len(content)):
                content_new = " ".join(content[aaa].split())
                vvv.setdefault('ip', content_new.split(" ")[0])
                vvv.setdefault('mac', content_new.split(" ")[3])
                vvv.setdefault('nic', content_new.split(" ")[5])
                arp_dic.setdefault(iii,vvv)
                vvv = {}
                iii = iii+1
        save_in_file.save_in_file(cont_all,self.get_class_name(),arp_dic)
        return arp_dic