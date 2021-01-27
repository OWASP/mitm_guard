import ipaddress
class listen_conns:
    def __init__(self, conns, internal_subnets, cont_all_local,ip_valid,all_ps):
        self.lis_conn = self.lis_conns(conns,internal_subnets,cont_all_local,ip_valid,all_ps)
    def get_class_name(self):
        return self.__class__.__name__
    def lis_conns(self,conns,internal_subnets,cont_all_local,ip_valid,all_ps):
        all_listen = {}
        all_dict_listen = {}
        list_all_dict_listen = {}
        ilisten = 0
        spec_in_nic = []
        validate = None
        for in_conns in range(len(conns)):
            validate = ip_valid.ipv4_valid(conns[in_conns][3][0])
            if (conns[in_conns][5] == "LISTEN") and ((conns[in_conns][3][0] == '::1') or (conns[in_conns][3][0] == '127.0.0.1')):
                pass
            elif (str(conns[in_conns][2]) != 'SocketKind.SOCK_DGRAM') &\
                 (conns[in_conns][5] == "LISTEN") & (validate.ip_val):
                proc_name = all_ps.all_ps(conns[in_conns][6])
                for in_inter in range(len(internal_subnets)):
                    if conns[in_conns][3][0] == '0.0.0.0':
                        spec_in_nic = ["None",conns[in_conns][3][0],"None","None","None","None"]
                    elif ipaddress.IPv4Address(conns[in_conns][3][0]) in ipaddress.IPv4Network(internal_subnets[in_inter][1]):
                        spec_in_nic = [internal_subnets[in_inter][0],internal_subnets[in_inter][1],\
                                                   internal_subnets[in_inter][2],internal_subnets[in_inter][3],\
                                                   internal_subnets[in_inter][4],internal_subnets[in_inter][5]]
                all_listen.setdefault('l_ip', conns[in_conns][3][0])
                all_listen.setdefault('l_p', conns[in_conns][3][1])
                all_listen.setdefault('st_c', conns[in_conns][5])
                all_listen.setdefault('i_ni', spec_in_nic[0])
                all_listen.setdefault('i_su', spec_in_nic[1])
                all_listen.setdefault('i_g', spec_in_nic[2])
                all_listen.setdefault('i_m', spec_in_nic[3])
                all_listen.setdefault('i_g_s', spec_in_nic[4])
                all_listen.setdefault('ip_v', str(conns[in_conns][1]))
                all_listen.setdefault('pr', str(conns[in_conns][2]))
                all_listen.setdefault('p_n', proc_name.p_name)
                all_listen.setdefault('pid', conns[in_conns][6])
                ilisten = ilisten+1
                list_all_dict_listen.setdefault(ilisten, all_listen)
                all_listen = {}
        cont_all_local.setdefault(self.get_class_name(),list_all_dict_listen)
        return list_all_dict_listen
