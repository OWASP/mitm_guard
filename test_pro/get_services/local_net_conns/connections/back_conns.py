class back_conns():
    def __init__(self, result_estab, result_listen, cont_all_local):
        self.back_connections = self.backreverse_conns(result_estab, result_listen, cont_all_local)
    def get_class_name(self):
        return self.__class__.__name__
    def backreverse_conns(self, result_estab, result_listen, cont_all_local):
        all_dict_back = {}
        cont_back = {}
        list_ports_listen = []
        list_ports_estab = []
        result_list_ports_back = []
        all_conn_back = {}
        iback = 0
        for in_listen in range(len(result_listen)):
            list_ports_listen.append(result_listen[in_listen+1]['l_p'])
        for in_result in range(len(result_estab)):
            list_ports_estab.append(result_estab[in_result+1]['l_p'])
        for in_in_len_b in range(0,len(list_ports_estab),1):
            for in_in_len_a in range(0,len(list_ports_listen),1):
                if list_ports_estab[in_in_len_b] not in list_ports_listen:
                    if list_ports_estab[in_in_len_b] not in result_list_ports_back:
                        result_list_ports_back.append(list_ports_estab[in_in_len_b])
        for len_result_list_ports_back in range(len(result_list_ports_back)):
            for in_result in range(len(result_estab)):
                if result_list_ports_back[len_result_list_ports_back] == result_estab[in_result+1]['l_p']:
                   all_conn_back.setdefault('l_ip', result_estab[in_result+1]['l_ip'])
                   all_conn_back.setdefault('l_p', result_estab[in_result+1]['l_p'])
                   all_conn_back.setdefault('d_ip', result_estab[in_result+1]['d_ip'])
                   all_conn_back.setdefault('d_p', result_estab[in_result+1]['d_p'])
                   all_conn_back.setdefault('st_c', result_estab[in_result+1]['st_c'])
                   all_conn_back.setdefault('i_ni', result_estab[in_result+1]['i_ni'])
                   all_conn_back.setdefault('i_su', result_estab[in_result+1]['i_su'])
                   all_conn_back.setdefault('i_g', result_estab[in_result+1]['i_g'])
                   all_conn_back.setdefault('i_m', result_estab[in_result+1]['i_m'])
                   all_conn_back.setdefault('i_g_s', result_estab[in_result+1]['i_g_s'])
                   all_conn_back.setdefault('i_dg', result_estab[in_result+1]['i_dg'])
                   all_conn_back.setdefault('e_su', result_estab[in_result+1]['e_su'])
                   all_conn_back.setdefault('ip_v', result_estab[in_result+1]['ip_v'])
                   all_conn_back.setdefault('pr', result_estab[in_result+1]['pr'])
                   all_conn_back.setdefault('p_n', result_estab[in_result+1]['p_n'])
                   all_conn_back.setdefault('pid', result_estab[in_result+1]['pid'])
                   iback = iback+1
                   cont_back.setdefault(iback, all_conn_back)
                   all_conn_back = {}
        cont_all_local.setdefault(self.get_class_name(),cont_back)
        return cont_back
