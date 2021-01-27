import ipaddress
class estab_conns:
    def __init__(self, conns,internal_subnets,cont_all_local,ip_valid,all_ps):
        self.estab_conn = self.estabilished_conns(conns,internal_subnets,cont_all_local,ip_valid,all_ps)
    def get_class_name(self):
        return __class__.__name__
    def estabilished_conns(self,conns,internal_subnets,cont_all_local,ip_valid,all_ps):
        all_dict_estab = {}
        all_estab = {}
        list_all_dict_estab = {}
        iestab = 0
        validate = False
        for in_conns_estab in range(len(conns)):
            validate = ip_valid.ipv4_valid(conns[in_conns_estab][3][0])
            if conns[in_conns_estab][5] == "ESTABLISHED" and validate.ip_val and \
               conns[in_conns_estab][3][0] == conns[in_conns_estab][4][0]:
                pass
            elif (conns[in_conns_estab][5] == "ESTABLISHED") and (validate.ip_val):
                spec_in_nic = []
                specs_external_nic = None
                proc_name = all_ps.all_ps(conns[in_conns_estab][6])
                for in_inter in range(len(internal_subnets)):
                   if ipaddress.IPv4Address(conns[in_conns_estab][3][0]) in ipaddress.IPv4Network(internal_subnets[in_inter][1]):
                      spec_in_nic = [internal_subnets[in_inter][0],internal_subnets[in_inter][1],\
                                                 internal_subnets[in_inter][2],internal_subnets[in_inter][3],\
                                                 internal_subnets[in_inter][4],internal_subnets[in_inter][5]]
                for in_inter in range(len(internal_subnets)):
                    if ipaddress.IPv4Address(conns[in_conns_estab][4][0]) in ipaddress.IPv4Network(internal_subnets[in_inter][1]):
                       specs_external_nic = internal_subnets[in_inter][1]
                all_estab.setdefault('l_ip', conns[in_conns_estab][3][0])
                all_estab.setdefault('l_p', conns[in_conns_estab][3][1])
                all_estab.setdefault('d_ip', conns[in_conns_estab][4][0])
                all_estab.setdefault('d_p', conns[in_conns_estab][4][1])
                all_estab.setdefault('st_c', conns[in_conns_estab][5])
                all_estab.setdefault('i_ni', spec_in_nic[0])
                all_estab.setdefault('i_su', spec_in_nic[1])
                all_estab.setdefault('i_g', spec_in_nic[2])
                all_estab.setdefault('i_m', spec_in_nic[3])
                all_estab.setdefault('i_g_s', spec_in_nic[4])
                all_estab.setdefault('i_dg', spec_in_nic[5])
                all_estab.setdefault('e_su', specs_external_nic)
                all_estab.setdefault('ip_v', str(conns[in_conns_estab][1]))
                all_estab.setdefault('pr', str(conns[in_conns_estab][2]))
                all_estab.setdefault('p_n', proc_name.p_name)
                all_estab.setdefault('pid', conns[in_conns_estab][6])
                iestab = iestab+1
                list_all_dict_estab.setdefault(iestab, all_estab)
                all_estab = {}
        cont_all_local.setdefault(self.get_class_name(),list_all_dict_estab)
        return list_all_dict_estab
