from . import arp_spoofing
from ..get_services import create_json
import datetime
from subprocess import Popen, PIPE
from ..hips import operation
import subprocess
import json
import os
import re
import ast
class split_ag():
    def split_ag_op(self,op, logs_a, dir_path):
        with open(dir_path+'.setting', 'r') as read_file:
            agent_coll = json.load(read_file)
        attacker = {}
        logs = logs_a.return_cont_all
        if op:
            # agent_coll    ==>  {'DG': "{'ip': '192.168.100.1', 'mac': '38:bc:01:bf:bd:f9', 'nic': 'ens33'}", 'DNS': "{'ip': ' ', 'mac': ' '}", 'DHCP': "{'ip': ' ', 'mac': ' '}", 'UUID': '155e4d56-f681-bdf5-e7ca-81f34cda0ef2', 'ID_Con': '1', 'Port': '51111', 'Setup_Date': '2020-09-13 14:45:53.871615'}
            # operation     ==>  '1', "{'ip': '172.16.1.1', 'mac': '00:0c:42:c3:f8:03', 'nic': 'ens33'}", "{'ip attacker': '172.16.1.116', 'mac attacker': '2c:59:e5:00:f1:03', 'nic': 'ens33'}", '15']
            # get_arp_cache ==> {1: {'ip': '192.168.1.4', 'mac': '00:0c:29:d9:ee:91', 'nic': 'enp0s25'},
                                #2: {'ip': '192.168.1.3', 'mac': '00:1f:fb:34:83:52', 'nic': 'enp0s25'},
                                #3: {'ip': '192.168.1.1', 'mac': '00:1f:fb:34:83:52', 'nic': 'enp0s25'}}
            if "arp_cache" in logs:
                ret_arp = arp_spoofing.arp_spoofing(agent_coll, logs_a, dir_path).ret
                if type(ret_arp) is dict:
                    exist_dir = os.path.isdir(dir_path)
                    exist_file = os.path.isfile(dir_path+'.attack_logs')
                    if not exist_dir:
                        os.system('mkdir '+dir_path)
                    else:
                        pass
                    if not exist_file:
                        i = 1
                        os.system('touch '+dir_path+".attack_logs")
                        f_logs = open(dir_path+".attack_logs", 'a')
                    else:
                        pass
                    split_ret_arp = self.op(recieve_op)
                    ret_arp_key =  ret_arp.keys()
                    if split_ret_arp is dict:
                        for gw in range(len((agent_coll["DG"]).keys())):
                            if (agent_coll['DG'][str(gw+1)]['ip'] == split_ret_arp[2]):
                                operation.operation(("1" + "-" +str(agent_coll['DG'][str(gw+1)]) + "-" + str(split_ret_arp) + "-" + "15"))
                                #operation = operation(("1" + "-" +str(agent_coll['DG']) + "-" + str(ret_arp) + "-" + "15"))
                                #so_conn.send(("1" + "-" +str(agent_coll['DG']) +logs"-" + str(ret_arp) + "-" + "15").encode())
                                #subprocess.Popen(["python", "warning_alarm.py"], stdout=subprocess.PIPE)
                                if (agent_coll['DG'][str(gw+1)]['ip'] == agent_coll['DNS'][str(gw+1)]['ip']) and (agent_coll['DG'][str(gw+1)]['ip'] == agent_coll['DHCP'][str(gw+1)]['ip']):
                                    ret_arp_key = ret_arp.keys()
                                    if "ip attacker" in ret_arp_key:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_ip":ret_arp["ip attacker"],"attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing','dns_spoofing','dhcp_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                                    else:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing','dns_spoofing','dhcp_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                                elif (agent_coll['DG'][str(gw+1)]['ip'] == agent_coll['DNS'][str(gw+1)]['ip']) and (agent_coll['DG'][str(gw+1)]['ip'] != agent_coll['DHCP'][str(gw+1)]['ip']):
                                    if "ip attacker" in ret_arp_key:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_ip":ret_arp["ip attacker"],"attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing','dns_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                                    else:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing','dns_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                elif (agent_coll['DG'][str(gw+1)]['ip'] != agent_coll['DNS'][str(gw+1)]['ip']) and (agent_coll['DG'][str(gw+1)]['ip'] == agent_coll['DHCP'][str(gw+1)]['ip']):
                                    if "ip attacker" in ret_arp_key:
                                        f_logs = open(dir_path+'/.'+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_ip":ret_arp["ip attacker"],"attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing','dhcp_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                                    else:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing','dhcp_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                                elif (agent_coll['DG'][str(gw+1)]['ip'] != agent_coll['DNS'][str(gw+1)]['ip']) and (agent_coll['DG'][str(gw+1)]['ip'] != agent_coll['DHCP'][str(gw+1)]['ip']):
                                    if "ip attacker" in ret_arp_key:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_ip":ret_arp["ip attacker"],"attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                                    else:
                                        f_logs = open(dir_path+"attack_logs", 'a')
                                        attacker = {"type_attack":"arp_spoofing","attacker_mac":ret_arp["mac attacker"],"risk":['arp_spoofing'],"victim":agent_coll['IP'][str(gw+1)],"date":datetime.datetime.now()}
                                        json_loads_attacker = create_json.json_dic.ret_json(attacker)
                                        f_logs.write(str(json_loads_attacker)+'\n')
                                        f_logs.close()
                elif ret_arp == "CG":
                    #so_conn.send(("Change device of gateway").encode())
                    print("Change device of gateway")

                elif ret_arp == "NA":
                    #so_conn.send(("No Attack").encode())
                    print("No Attack")
                else:
                    #no recieve log of arp
                    pass
            else:
                so_conn.send(("Other processing").encode())
        else:
            pass
    def op(self,recieve_op):
        ch = "-"
        search = re.search(ch,recieve_op)
        if bool(search):
            attack_info = recieve_op.split("-")
            #attack_info ==> ['1', "{'ip': '172.16.1.1', 'mac': '00:0c:42:c3:f8:03', 'nic': 'ens33'}", "{'ip attacker': '172.16.1.116', 'mac attacker': '2c:59:e5:00:f1:03', 'nic': 'ens33'}", '15']
        else:
            return False