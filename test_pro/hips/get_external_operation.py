import re
import os
import ast
import json
import os
from ..communications import p_listen, agent_coms
class get_external_operation:
    def __init__(self, inter_subs, arp_cache, addr, conn, dir_path):
        self.ret = self.op(inter_subs, arp_cache, addr, conn, dir_path)

    def op(self, inter_subs, arp_cache, addr, conn, dir_path):
        #get_data = conn.recv(1024).decode()
        #aaaa = {'attacker_ip': 'no detect hacker ip', 'attacker_mac': '00:0c:29:fa:f5:cd', 'num': '6'}
        attack_info = ast.literal_eval(str(conn.recv(1024).decode()))
        self.arp_spoofing(addr, conn, attack_info, dir_path)

    def arp_spoofing(self, inter_subs, arp_cache, addr, conn, att, dir_path):
        #GW(att_1) ==> {'ip': '172.16.1.1', 'mac': '00:0c:42:c3:f8:06', 'nic': 'ens33'}
        #ATTACKER(att_2) ==> {'attacker_ip': '172.16.1.116', 'attacker_mac': '2c:59:e5:00:f1:03', 'nic': 'ens33'}
        data = {}
        with open(dir_path+".setting", 'r') as read_file:
            agent_coll = json.load(read_file)
        for gw in range(len((agent_coll["DG"]).keys())):
            if int(att["num"]) == 1:
                attacker_ip = self.search_mac_log(self, agent_coll['DG'][str(gw+1)]['ip'], att["attacker_mac"], arp_cache)
                if attacker_ip:
                    att['attacker_ip'] = attacker_ip
                    att["num"] = 2
                    os.system("arp -s " + agent_coll['DG'][str(gw+1)]['ip'] + " " + agent_coll['DG'][str(gw+1)]['mac'])
                    os.system("arp -s " + att["attacker_ip"] + " "+att["attacker_mac"])
                    conn.send((str(att)).encode())
                    read_file.close()
                    return "Clear"
                else:
                    att["num"] == 3
                    os.system("arp -s " + agent_coll['DG'][str(gw+1)]['ip'] + " " + agent_coll['DG'][str(gw+1)]['mac'])
                    conn.send((str(att)).encode())
                    read_file.close()
                    return "Clear"
            elif int(att["num"]) == 2:
                os.system("arp -s " + agent_coll['DG'][str(gw+1)]['ip'] + " " + agent_coll['DG'][str(gw+1)]['mac'])
                os.system("arp -s " + att["attacker_ip"] + " "+att["attacker_mac"])
                att["num"] = 9
                self.publish_to_neighbors(self, inter_subs, path, att)
                read_file.close()
                return "Clear"
            elif int(att["num"]) == 3:
                read_file.close()
                return "Clear"
            elif int(att["num"]) == 6:
                os.system("arp -s " + agent_coll['DG'][str(gw+1)]['ip'] + " " + agent_coll['DG'][str(gw+1)]['mac'])
                conn.send((str({'num': '1'})).encode())
                read_file.close()
                return "Clear"
            elif int(att["num"]) == 9:
                #att_1 = ast.literal_eval(att[1])
                os.system("arp -s "+agent_coll['DG'][str(gw+1)]['ip']+" "+agent_coll['DG'][str(gw+1)]['mac'])
                os.system("arp -s "+att["attacker_ip"]+" "+att["attacker_mac"])
                print("Detect ARP_Spoofing in the network", att["attacker_ip"])
                print("Informations of Attacker are:", att)
                print("Prevention is done ...")
                conn.send((str({'num': '1'})).encode())
                read_file.close()
                return "Clear"
            else:
                pass

    def search_mac_log(self, exclude_ip, mac, arp):
        ip = "not"
        for lo in range(len(arp)):
            if (arp[str(lo+1)]['mac'] == mac):
                ip = arp[str(lo+1)]['ip']
            else:
                pass
        if ip != "not":
            return ip
        else:
            return ip
    def publish_to_neighbors(self, inter_subs, path, attacker):
        neighs = (neighbors.neighbors(inter_subs, path, attacker)).p_scanner
        n_keys = list(aaa.keys())
        for n in range(len(n_keys)):
            for m in range(len(neighs[n_keys[n]])):
                conn_sock = (agent_coms.agent_coms(neighs[n_keys[n]][str(m+1)]["ip"],neighs[n_keys[n]][str(m+1)]["port"])).agent_com
                conn_sock.send((str(attacker)).encode())