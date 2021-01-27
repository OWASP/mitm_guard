import json
import hashlib
from . import create_json ,ret_cont_all
import datetime
class compare_content:
    def __init__(self, location, prev_hash, new_hash, new_content):
        self.ret = self.compare_cont(location, prev_hash, new_hash, new_content)
    ################################################
    ############ Start Compare Function ############
    def compare_cont(self,location, prev_hash, new_hash, new_content):
        null_dict = "99914b932bd37a50b983c5e7c90ae93b"
        if (new_hash != prev_hash) and (new_hash != null_dict):
            f_w = open(location+".arp_cache", 'w')
            f_w.writelines(new_hash)
            f_w.close()
            f_logs = open(location+".logs", 'a')
            f_logs.write('\n'+str((ret_cont_all.ret_cont_all(new_content['arp_cache'])).c_all))
            f_logs.close()
            return True
        elif new_hash == prev_hash:
            return False
            #print("null_content")
    ############# End Compare Function #############
    ################################################
