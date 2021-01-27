from . import local_net_conns as local_conns
class port_scanner:
    def __init__(self, port_num, status_conn):
        self.p_scanner = self.special_port_scanner(port_num, status_conn)
    def special_port_scanner(self, port_num, status_conn):
        if status_conn == "listen":
            port_status = local_conns.estab_conns.estab_conn
            dict_key = port_status.keys()
            for lendict in dict_key:
                if port_status[lendict]['l_p'] == port_num:
                    return True
        elif status_conn == "estab":
            port_status = local_conns.listen_conns.lis_conn
            dict_key = port_status.keys()
            for lendict in dict_key:
                if port_status[lendict]['l_p'] == port_num:
                    return True
        elif status_conn == "simul":
            port_status = local_conns.simul_conns.simultaneously_conns
            dict_key = port_status.keys()
            for lendict in dict_key:
                if port_status[lendict]['l_p'] == port_num:
                    return True
        elif status_conn == "back":
            port_status = local_conns.back_conns.back_connections
            dict_key = port_status.keys()
            for lendict in dict_key:
                if port_status[lendict]['d_p'] == port_num:
                    return True
