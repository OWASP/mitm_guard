import os
import json
import hashlib

class save_in_file:
    def __init__(self,cont_all,file_name,data):
        loc_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = str('/'+loc_path.split('/')[1])+str('/'+loc_path.split('/')[2])+"/.run_agent/"
        #print("aaaaaaa",data)
        stri = json.dumps(data)
        stri = hashlib.md5(stri.encode())
        exist_dir = os.path.isdir(dir_path)
        exist_file = os.path.isfile(dir_path+'.'+file_name)
        null_dict = "99914b932bd37a50b983c5e7c90ae93b"
        if exist_dir and exist_file:
            with open(dir_path+'.'+file_name) as file:
                first = file.read(1)
            if not first:
                f_w = open(dir_path+'.'+file_name, 'w')
                f_w.writelines(stri.hexdigest())
                f_w.close()
                cont_all.setdefault(file_name,data)
            else:
                f_r = open(dir_path+'.'+file_name, 'r')
                content = f_r.readline()
                f_r.close()
                f_w = open(dir_path+'.'+file_name, 'w')
                if (stri.hexdigest() != content) and (stri.hexdigest() != null_dict):
                    cont_all.setdefault(file_name,data)
                    f_w.writelines(stri.hexdigest())
                    f_w.close()
                    #print("True : "+file_name)
                else:
                    f_w.writelines(stri.hexdigest())
                    f_w.close()
                    #print("equal : "+file_name)
        elif exist_dir and not exist_file:
            os.system('touch '+dir_path+'.'+file_name)
            f_w = open(dir_path+'.'+file_name, 'w')
            f_w.writelines(stri.hexdigest())
            f_w.close()
            cont_all.setdefault(file_name,data)
            
            #print("True not exist_file : "+file_name)
        elif not exist_dir:
            os.system('mkdir '+dir_path)
            os.system('touch '+dir_path+'.'+file_name)
            f_w = open(dir_path+'.'+file_name, 'w')
            f_w.writelines(stri.hexdigest())
            f_w.close()
            cont_all.setdefault(file_name,data)
            
            #print("True not exist_dir : "+file_name)
