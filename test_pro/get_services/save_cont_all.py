import os
import hashlib
import json
class save_cont_all:
    def __init__(self,file_name,location,all_result):
        self.get_act = self.action(file_name,location,all_result)
    def action(self,file_name,location,all_result):
        #print(all_result)
        null_dict = "99914b932bd37a50b983c5e7c90ae93b"
        cont_all = json.dumps(all_result)
        cont_all = hashlib.md5(cont_all.encode())
        exist_file = os.path.isfile(location+'/.'+file_name)
        if exist_file:
            with open(location+'/.'+file_name) as file:
                first = file.read(1)
                file.close()
            if not first:
                f_w = open(location+'/.'+file_name, 'w')
                os.system('touch '+location+'/.'+file_name)
                f_w = open(location+'/.'+file_name, 'w')
                f_w.writelines(cont_all.hexdigest())
                f_w.close()
                return True
            else:
                f_r = open(location+'/.'+file_name, 'r')
                content = f_r.readline()
                f_r.close()
                f_w = open(location+'/.'+file_name, 'w')
                if cont_all.hexdigest() != content:
                    f_w.writelines(cont_all.hexdigest())
                    f_w.close()
                    return True
                else:
                    f_w.writelines(cont_all.hexdigest())
                    f_w.close()
        elif not exist_file:
            os.system('touch '+location+'/.'+file_name)
            f_w = open(location+'/.'+file_name, 'w')
            f_w.writelines(cont_all.hexdigest())
            f_w.close()
            return True
