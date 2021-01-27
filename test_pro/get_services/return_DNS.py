from . import create_json
import os
from scapy.all import *
class return_DNS:
    def __init__(self,ip_add):
        self.ret = self.ret_dns(ip_add)
    def ret_dns(self,ip_add):
        dns = {}
        ALL_DNS = {}
        inum = 0
        x = re.split("\n", (subprocess.check_output(["systemd-resolve --status | grep 'Current DNS Server'"], stderr=subprocess.STDOUT,shell=True)).decode("utf-8"))
        while '' in x:
            x.remove('')
        for i in range(len(ip_add)):
            dns_ip = ((list(reversed(x))[i]).replace(' ', '')).split(":")[1]
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=dns_ip),timeout=1, iface=ip_add[i][0])
            for sent, received in ans:
                mac = str(received[ARP].hwsrc)
            dns.setdefault('ip',dns_ip)
            dns.setdefault('mac',mac)
            dns.setdefault('nic',str(ip_add[i][0]))
            inum = inum+1
            ALL_DNS.setdefault(inum, dns)
            dns = {}
        return ALL_DNS
        