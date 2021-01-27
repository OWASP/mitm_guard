import re
import os
import ast
class operation:
    def __init__(self,recieve_op):
        self.ret = self.attack_prevention(recieve_op)
    def attack_prevention(self,att_num):
        if int(att_num[0]) == 1:
            return self.arp_spoofing(att_num)
        else:
            pass
    def arp_spoofing(self,att):
        #recieve ==> "1" + "-" +str(dic_DG) + "-" + str(ret_arp) + "-" + "15"
        if int(att[3]) == 15:
            #GW(att_1) ==> {'ip': '172.16.1.1', 'mac': '00:0c:42:c3:f8:06', 'nic': 'ens33'}
            #ATTACKER(att_2) ==> {'ip attacker': '172.16.1.116', 'mac attacker': '2c:59:e5:00:f1:03', 'nic': 'ens33'}
            log_keys = ast.literal_eval(att[2]).keys()
            if "ip attacker" in log_keys:
                att_1 = ast.literal_eval(att[1])
                att_2 = ast.literal_eval(att[2])
                os.system("arp -s "+att_1['ip']+" "+att_1['mac'])
                os.system("arp -s "+att_2['ip attacker']+" "+att_2['mac attacker'])
                return "Clear"
            else:
                att_1 = ast.literal_eval(att[1])
                os.system("arp -s "+att_1['ip']+" "+att_1['mac'])
                return "Clear"
