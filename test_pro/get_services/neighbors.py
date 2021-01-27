import xml.etree.ElementTree as ET
import subprocess
from xml.dom import minidom
from . import create_json
import json
class neighbors:
    def __init__(self, inter_subs, path):
        self.p_scanner = self.special_port_scanner(inter_subs, path)
    def special_port_scanner(self, inter_subs, path):
        #inter_subs[['ens33', '192.168.100.0/24', '192.168.100.1', '00:0c:29:da:0e:f2', True, '192.168.100.1', '192.168.100.219'], ['ens38', '192.168.244.0/24', '192.168.244.2', '00:0c:29:da:0e:fc', True, '192.168.100.1', '192.168.244.136']]
        with open(path+'.neighbors.json', 'w') as outfile:
            with open(path+".setting", 'r') as read_file:
                agent_coll = json.load(read_file)
            neigh_ip = {} 
            result_per_sub = {}
            result_all_sub = {}
            for m in range(len(inter_subs)):
                output = subprocess.check_output(["nmap", "-p", agent_coll['Port'], "-n", inter_subs[m][1], "-e", inter_subs[m][0], "-oX", "-"], stderr=subprocess.STDOUT)
                num = 0
                #xmldoc = minidom.parse('test.xml')
                xmldoc = minidom.parseString(output)
                itemlist = xmldoc.getElementsByTagName('host')
                #print(inter_subs[m][0], itemlist)
                for n in range(len(itemlist)):
                    #ports = (itemlist[n].getElementsByTagName('ports'))[0]
                    #port = (ports).getElementsByTagName('port')[0]
                    #portid = (port).attributes['portid'].value
                    #state = (portid).getElementsByTagName("state")[0]
                    state = ((((itemlist[n].getElementsByTagName('ports'))[0]).getElementsByTagName('port')[0]).getElementsByTagName("state")[0]).attributes['state'].value
                    if state == "open":
                        #ip_element = (itemlist[n].getElementsByTagName('address'))[0]
                        #mac_element = (itemlist[n].getElementsByTagName('address'))[1]
                        #portid = port.attributes['portid'].value
                        #ip = ip_element.attributes['addr'].value
                        #mac = mac_element.attributes['addr'].value
                        neigh_ip.setdefault("ip", ((itemlist[n].getElementsByTagName('address'))[0]).attributes['addr'].value)
                        neigh_ip.setdefault("mac", ((itemlist[n].getElementsByTagName('address'))[1]).attributes['addr'].value)
                        neigh_ip.setdefault("port", (((itemlist[n].getElementsByTagName('ports'))[0]).getElementsByTagName('port')[0]).attributes['portid'].value)
                        neigh_ip.setdefault("state", state)
                        num = num+1
                        result_per_sub.setdefault(str(num), neigh_ip)
                        neigh_ip = {}
                result_all_sub.setdefault(inter_subs[m][0], result_per_sub)
                result_per_sub = {}
            json.dump(result_all_sub, outfile)
            outfile.close()
            return json.dumps(result_all_sub)