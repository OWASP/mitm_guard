import datetime
import threading
import aaa
import bbb
import time
import json
import os
import hashlib
from test_pro.get_services import run_agent, compare_content, os_funs, port_scanner, agent_coms, ret_cont_all, create_json, neighbors
from test_pro.hips import operation, get_external_operation
from test_pro.hids import split_ag_op
from test_pro.communications import p_listen, agent_coms
import test_pro
import socket
import xmltodict
import subprocess
def main():
    t1 = threading.Thread(name='loop_process', target=main_process)
    t1.start()
    t2 = threading.Thread(name='accept_data', target=accept_data)
    t2.start()
    time.sleep(1)
    t3 = threading.Thread(name='neighbors', target=(neighbors.neighbors(inter_subs, dir_path)).p_scanner)
    t3.start()
def accept_data():
    HOST = ''
    PORT = 51111 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
        print('Socket bind complete')
    s.listen(10)
    ret_operation = ""
    while True:
        conn, addr = s.accept()
        #print('Content ' + conn.recv(1024).decode())
        if conn:
            ret_operation = get_external_operation.get_external_operation(inter_subs, arp_cache, addr, conn, dir_path)
        if ret_operation != "":
            pass
            #print('external operation has been cleared')
        else:
            pass
            #print("I have not received anything")

def main_process(): 
    global inter_subs
    global arp_cache
    global dir_path
    loc_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = str('/'+loc_path.split('/')[1])+str('/'+loc_path.split('/')[2])+"/.run_agent/"
    ob_A = (aaa.aaa()).varA
    inter_subs = ob_A.inter_subnets
    arp_cache = ob_A.arp_caches
    id_agent = ob_A.id_agent
    spl = split_ag_op.split_ag()
    all_result = ob_A.return_cont_all
    all_result.setdefault("date",str(datetime.datetime.now()))
    exist_file = os.path.isfile(dir_path+'.logs')
    if not exist_file:
        i = 1
        os.system('touch '+dir_path+'.logs')
        logs = open(dir_path+'.logs', 'w')
        logs.write(str((ret_cont_all.ret_cont_all(all_result)).c_all))
        logs.close()
    else:
        pass
    while True:
        f_r = open(dir_path+'.arp_cache', 'r')
        prev_hash_content = f_r.readline()
        f_r.close()
        time.sleep(1)
        ob_B = (bbb.bbb()).varB
        new_result = ob_B.return_cont_all
        new_result.setdefault("date",str(datetime.datetime.now()))
        if bool(new_result):
            ######## Compare previous hash with current hash
            if "arp_cache" in new_result.keys():
                new_hash_content = json.dumps(new_result['arp_cache'])
                new_hash_content = (hashlib.md5(new_hash_content.encode())).hexdigest()
                result = (compare_content.compare_content(dir_path, prev_hash_content, new_hash_content, new_result)).ret
                if bool(result):
                    spl.split_ag_op("True", ob_B, dir_path)
            else:
                #print("nothing arp_cache")
                pass

if __name__ == "__main__":
    main()