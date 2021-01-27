from ..get_services import neighbors
from ..communications import p_listen, agent_coms
import ipaddress
import json
class arp_spoofing:
    def __init__(self, agent_coll, logs_a, dir_path):
        self.ret = self.ret_arp_spoof_attackers(agent_coll, logs_a, dir_path)
    def ret_arp_spoof_attackers(self, agent_coll, logs_a, dir_path):
        #log_a ==> this is object
        #attacker ==> attacker detection
        #CG ==> Change Gateway device
        #NA ==> No Attack arp poisoning
        #NG ==> no find device of gateway
        #get_arp_cache ==> realtime arp_cache
        #agent_coll ==> {"IP": {"1": "192.168.100.219", "2": "192.168.244.136"}, "DG": {"1": {"ip": "192.168.100.1", "mac": "38:bc:01:bf:bd:f9", "nic": "ens33"}, "2": {"ip": "192.168.244.2", "mac": "00:50:56:e0:db:7c", "nic": "ens38"}}, "DNS": {"1": {"ip": "192.168.100.1", "mac": "38:bc:01:bf:bd:f9", "nic": "ens33"}, "2": {"ip": "192.168.244.2", "mac": "00:50:56:e0:db:7c", "nic": "ens38"}}, "DHCP": {"ip": " ", "mac": " "}, "UUID": "155e4d56-f681-bdf5-e7ca-81f34cda0ef2", "ID_Con": "1", "Port": "80", "Setup_Date": "2020-11-18 10:55:58.375394"}
        #log = {1: {'ip': '192.168.1.4', 'mac': '00:0c:29:d9:ee:91', 'nic': 'enp0s25'},
               #2: {'ip': '192.168.1.3', 'mac': '00:1f:fb:34:83:52', 'nic': 'enp0s25'},
               #3: {'ip': '192.168.1.1', 'mac': '00:1f:fb:34:83:52', 'nic': 'enp0s25'}}
        #sample of arp response: {'192.168.100.1': '38:bc:01:bf:bd:f9', '192.168.100.219': '00:0c:29:da:0e:f2'}
        #get_gw ==> log[m+1] : {'ip': '192.168.1.4', 'mac': '00:0c:29:d9:ee:91', 'nic': 'enp0s25'}
        #search_log ==> log[m+1]['ip'] : '192.168.1.1'
        attacker = {}
        ip_attacker = ""
        ni_list = ""
        #NG ==> no find device of gateway
        log = logs_a.arp_caches
        #get_gw = self.search_gw_log(agent_coll['DG']['ip'],log)
        with open(dir_path+".neighbors.json", 'r') as read_file:
            neighbors = json.load(read_file)
        for gw in range(len((agent_coll["DG"]).keys())):
            for m in range(len(log)):
                get_ip_from_mac = self.search_mac_log(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], log)
                get_mac_except = self.get_mac_except_gw(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], log)
                if (agent_coll['DG'][str(gw+1)]['ip'] != log[m+1]['ip']) & (agent_coll['DG'][str(gw+1)]['mac'] != log[m+1]['mac']):
                    pass
                elif (agent_coll['DG'][str(gw+1)]['ip'] != log[m+1]['ip']) & (get_ip_from_mac != "not"):
                    attacker.setdefault("attacker_ip",log[m+1]['ip']) #getmac == ip address
                    attacker.setdefault("attacker_mac",log[m+1]['mac'])
                    attacker.setdefault("gateway_ip",agent_coll['DG'][str(gw+1)]['ip'])
                    attacker.setdefault("num","9")
                    publish_to_neighbors(logs_a.inter_subnets, dir_path, attacker)
                    print("1")
                    print("Detecting ARP_Spoofing Attack")
                    print("Informations of Attacker are:: ",attacker)
                    print("Publish to all agents")
                    return attacker
                elif (agent_coll['DG'][str(gw+1)]['ip'] != log[m+1]['ip']) & (get_ip_from_mac == "not"):
                    pass
                elif (agent_coll['DG'][str(gw+1)]['ip'] == log[m+1]['ip']) & (agent_coll['DG'][str(gw+1)]['mac'] != log[m+1]['mac']):
                    if get_mac_except != "not":
                        attacker.setdefault("attacker_ip",get_mac_except)
                        attacker.setdefault("attacker_mac",log[m+1]['mac'])
                        attacker.setdefault("gateway_ip",agent_coll['DG'][str(gw+1)]['ip'])
                        attacker.setdefault("num","9")
                        publish_to_neighbors(logs_a.inter_subnets, dir_path, attacker)
                        print("2")
                        print("Detecting ARP_Spoofing Attack")
                        print("Informations of Attacker are:: ",attacker)
                        print("Publish to all agents")
                        return attacker
                    else:
                        ob_arp_req = (network_scan.ArpRequest()).get_ip_and_mac(agent_coll['DG'][str(gw+1)]['ip'])
                        if ob_arp_req is not None:
                            if agent_coll['DG'][str(gw+1)]['mac'] == ob_arp_req[agent_coll['DG'][str(gw+1)]['ip']]:
                                attacker.setdefault("attacker_ip","")
                                attacker.setdefault("attacker_mac",log[m+1]['mac'])
                                attacker.setdefault("gateway_ip",agent_coll['DG'][str(gw+1)]['ip'])
                                attacker.setdefault("num","1")
                                publish_to_neighbors(logs_a.inter_subnets, dir_path, attacker)
                                ni_list = self.net_scan(agent_coll['DG'][str(gw+1)]['ip'], log[m+1]['mac'], logs_a.all_subnets)
                                if ni_list:
                                    attacker.setdefault("attacker_ip",ni_list)
                                    attacker.setdefault("attacker_mac",log[m+1]['mac'])
                                    attacker.setdefault("gateway_ip",agent_coll['DG'][str(gw+1)]['ip'])
                                    attacker.setdefault("num","9")
                                    publish_to_neighbors(logs_a.inter_subnets, dir_path, attacker)
                                    print("3")
                                    print("Detecting ARP_Spoofing Attack")
                                    print("Informations of Attacker are:: ",attacker)
                                    print("Publish to all agents")
                                    return attacker
                                else:
                                    attacker.setdefault("attacker_ip","")
                                    attacker.setdefault("attacker_mac",log[m+1]['mac'])
                                    attacker.setdefault("num","3")
                                    random_net_scan(logs_a.inter_subnets, dir_path, attacker)
                                    print("4")
                                    print("Detecting ARP_Spoofing Attack")
                                    print("Informations of Attacker are:: ",attacker)
                                    print("Publish to all agents")
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

    def net_scan(self, ip, mac, sub_ranges):
        for n in range(len(sub_ranges)):
            if (IPv4Address(ip) in IPv4Network(sub_ranges[n][1])):
                scan_re = (re.split("\n", (subprocess.check_output(["nmap -sn " + sub_ip + " | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " "substr($0, index($0,$2)) }' | sort"], stderr=subprocess.STDOUT,shell=True)).decode("utf-8")))[:-2]
                for i in range(len(scan_re)):
                    line_spl = re.split("Address: ", scan_re[i])
                    if mac == (re.split(" ", line_spl[1]))[0]:
                        return line_spl[0]
                    else:
                        return False
            else:
                pass

    def publish_to_neighbors(self, inter_subs, path, attacker):
        neighs = (neighbors.neighbors(inter_subs, path, attacker)).p_scanner
        n_keys = list(aaa.keys())
        for n in range(len(n_keys)):
            for m in range(len(neighs[n_keys[n]])):
                conn_sock = (agent_coms.agent_coms(neighs[n_keys[n]][str(m+1)]["ip"],neighs[n_keys[n]][str(m+1)]["port"])).agent_com
                conn_sock.send((str(attacker)).encode())