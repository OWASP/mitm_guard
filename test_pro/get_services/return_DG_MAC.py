from . import create_json
import netifaces
from scapy.all import *
class return_DG_MAC:
    def __init__(self):
        self.ret = self.ret_dg_mac()
    def ret_dg_mac(self):
        store_GW ={}
        GWs = {}
        iback = 0
        all_gw = list(reversed((netifaces.gateways())[2]))
        for n in range(len(all_gw)):
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=all_gw[n][0]),timeout=1, iface=all_gw[n][1])
            for sent, received in ans:
                mac = str(received[ARP].hwsrc)
            store_GW.setdefault('ip',all_gw[n][0])
            store_GW.setdefault('mac',mac)
            store_GW.setdefault('nic',all_gw[n][1])
            iback = iback+1
            GWs.setdefault(iback, store_GW)
            store_GW = {}
        all_json_DG_agent = (create_json.create_json(GWs)).ret_json
        return all_json_DG_agent

"""
    def ret_dg_mac(self):
        store_GW ={}
        GWs = {}
        get_DG1 = (get_DG.get_DG()).g_dg
        iback = 0
        #print(get_DG1)
        re_get_arp = (get_arp.get_arp()).g_arp
        dic_keys = re_get_arp.keys()
        #print(dic_keys)
        #print(get_DG1)
        for i in range(len(get_DG1)):
            #print(re_get_arp)
            #print(get_DG1[i])
            for ind in range(len(dic_keys)):
                #print(dic_keys)
                if get_DG1[i] == re_get_arp[ind+1]["ip"]:
                    #print("okey")
                    #print("re_get_arp",re_get_arp[ind+1])
                    #print("get_DG1[i]",get_DG1[i])
                    store_GW.setdefault('ip',re_get_arp[ind+1]["ip"])
                    store_GW.setdefault('mac',re_get_arp[ind+1]["mac"])
                    store_GW.setdefault('nic',re_get_arp[ind+1]["nic"])
                    iback = iback+1
                    GWs.setdefault(iback, store_GW)
                    store_GW = {}
        all_json_DG_agent = (create_json.create_json(GWs)).ret_json
        return all_json_DG_agent
"""