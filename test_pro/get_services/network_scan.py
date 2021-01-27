from ..get_services import network_scan
from ..communications import p_listen, agent_coms
import ipaddress
import json
class arp_spoofing:
    def __init__(self, agent_coll, logs_a, dir_path):
        self.ret = self.ret_arp_spoof_attackers(agent_coll, logs_a, dir_path)
    def ret_arp_spoof_attackers(self, agent_coll, logs_a, dir_path):
        attacker = {}
        ip_attacker = ""
        ni_list = ""
        log = logs_a.arp_caches
        with open(dir_path+".neighbors.json", 'r') as read_file:
            neighbors = json.load(read_file)
        for gw in range(len((agent_coll["DG"]).keys())):
            for m in range(len(log)):
                get_ip_from_mac = self.search_mac_log(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], log)
                get_mac_except = self.get_mac_except_gw(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], log)
                if (agent_coll['DG'][str(gw+1)]['ip'] != log[m+1]['ip']) & (agent_coll['DG'][str(gw+1)]['mac'] != log[m+1]['mac']):
                    pass
                elif (agent_coll['DG'][str(gw+1)]['ip'] != log[m+1]['ip']) & (get_ip_from_mac != "not"):
                    attacker.setdefault("attacker_ip",log[m+1]['ip'])
                    attacker.setdefault("attacker_mac",log[m+1]['mac'])
                    publish_to_neighbors(attacker)
                    return attacker
                elif (agent_coll['DG'][str(gw+1)]['ip'] != log[m+1]['ip']) & (get_ip_from_mac == "not"):
                    pass
                elif (agent_coll['DG'][str(gw+1)]['ip'] == log[m+1]['ip']) & (agent_coll['DG'][str(gw+1)]['mac'] != log[m+1]['mac']):
                    if get_mac_except != "not":
                        attacker.setdefault("attacker_ip",get_mac_except)
                        attacker.setdefault("attacker_mac",log[m+1]['mac'])
                        publish_to_neighbors(attacker)
                        return attacker
                    else:
                        ob_arp_req = (network_scan.ArpRequest()).get_ip_and_mac(agent_coll['DG'][str(gw+1)]['ip'])
                        if ob_arp_req is not None:
                            if agent_coll['DG'][str(gw+1)]['mac'] == ob_arp_req[agent_coll['DG'][str(gw+1)]['ip']]:
                                attacker_ip = self.net_scan(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], logs_a.all_subnets)
                                if self.net_scan(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], logs_a.all_subnets):
                                    if attacker_ip:
                                        attacker.setdefault("attacker_ip",attacker_ip)
                                        attacker.setdefault("attacker_mac",log[m+1]['mac'])
                                        publish_to_neighbors(attacker)
                                        return attacker
                                    else:
                                        attacker.setdefault("attacker_ip","no detect")
                                        attacker.setdefault("attacker_mac",log[m+1]['mac'])
                                        publish_to_neighbors(attacker)
                                        return attacker
                        else:
                            print("no find gw")
                elif (agent_coll['DG'][str(gw+1)]['ip'] == log[m+1]['ip']) & (agent_coll['DG'][str(gw+1)]['mac'] == log[m+1]['mac']):
                    pass
                else:
                    pass

    def search_mac_log(self, exclude_ip, mac, log):
        ip = "not"
        for lo in range(len(log)):
            if (log[lo+1]['mac'] == mac) & (log[lo+1]['ip'] == exclude_ip):
                ip = log[lo+1]['ip']
        if ip != "not":
            return ip
        else:
            return ip

    def search_gw_log(self, dg_ip, arp_c):
        for m in range(len(arp_c)):
            if dg_ip == arp_c[m+1]['ip']:
                return arp_c[m+1]
            else:
                return "not"

    def get_mac_except_gw(self, exclude_ip, mac, log):
        ip = "not"
        for lo in range(len(log)):
            if (log[lo+1]['mac'] == mac) & (log[lo+1]['ip'] != exclude_ip):
                ip = log[lo+1]['ip']
        if ip != "not":
            return ip
        else:
            return "not"

    def net_scan(ip, mac, sub_ranges):
        for n in range(len(sub_ranges)):
            if (IPv4Address(ip) in IPv4Network(sub_ranges[n][1])):
                scan_re = (re.split("\n", (subprocess.check_output(["nmap -sn " + sub_ranges[n] + " | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " "substr($0, index($0,$2)) }' | sort"], stderr=subprocess.STDOUT,shell=True)).decode("utf-8")))[:-2]
                for i in range(len(scan_re)):
                    line_spl = re.split("Address: ", scan_re[i])
                    if mac == (re.split(" ", line_spl[1]))[0]:
                        return line_spl[0]
                    else:
                        return False
            else:
                pass
            