import netifaces
from netaddr import IPAddress
import netaddr
class in_subnets:
    def __init__(self, inters, cont_all_local):
        self.in_subs = self.internal_subnets(inters, cont_all_local)
    def get_class_name(self):
        return __class__.__name__
    def internal_subnets(self,inters, cont_all_local):
        mac_hw = []
        inic = 0
        list_all_local_nic = []
        dict_internal_nic = {}
        all_dict_inter = {}
        all_dict_inters = {}
        for interface_name in inters:
            remoteServer = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['addr']
            broadcast = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['broadcast']
            mac_hw = netifaces.ifaddresses(interface_name)[netifaces.AF_LINK]
            mac_hw = mac_hw[0]['addr']
            netmask = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['netmask']
            sss = IPAddress(netmask).netmask_bits()
            cidr = netaddr.IPNetwork('%s/%s' % (remoteServer, netmask))
            network = cidr.network
            subnet = '%s/%s' % (network, sss)
            gw = None
            default_gw_status = None
            default_gw = None
            gws = netifaces.gateways()
            for len_2 in range(len(gws[2])):
                if gws[2][len_2][1] == interface_name:
                    gw = gws[2][len_2][0]
                    default_gw = gws['default'][2][0]
                    default_gw_status = gws[2][len_2][2]
            list_all_local_nic.append([interface_name,subnet,gw,mac_hw,default_gw_status,default_gw,remoteServer])
        for ind_local_nic in range(len(list_all_local_nic)):
            inic = inic+1
            dict_internal_nic = {'local_nic':list_all_local_nic[ind_local_nic][0],
                                    'subnet':list_all_local_nic[ind_local_nic][1],
                                    'gateway_ip':list_all_local_nic[ind_local_nic][2],
                                    'mac_address':list_all_local_nic[ind_local_nic][3],
                                    'default_gateway':list_all_local_nic[ind_local_nic][4],
                                    'lead_default_gw_ip':list_all_local_nic[ind_local_nic][5]
                                      }
            all_dict_inter.setdefault(inic ,dict_internal_nic)
        cont_all_local.setdefault(self.get_class_name(),all_dict_inter)
        return list_all_local_nic