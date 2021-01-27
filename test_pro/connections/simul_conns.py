import ipaddress
from ..get_services import save_in_file
class simul_conns:
    def __init__(self, result_estab, result_listen, internal_subnets, cont_all):
        self.s_conns = self.simultaneously_listen_estab(result_estab, result_listen, internal_subnets, cont_all)
    def get_class_name(self):
        return self.__class__.__name__
    def simultaneously_listen_estab(self, result_estab, result_listen, internal_subnets, cont_all):
          all_dict_simul = {}
          cont_simul = {}
          all_listen = {}
          isimult = 0
          specs_external_nic = None
          for in_result in range(len(result_estab)):
              for in_listen in range(len(result_listen)):
                  if (result_estab[in_result+1]['l_ip'] and result_estab[in_result+1]['l_p']) == \
                     (result_listen[in_listen+1]['l_ip'] and result_listen[in_listen+1]['l_p']):
                     for in_inter in range(len(internal_subnets)):
                         if ipaddress.IPv4Address(result_estab[in_result+1]['d_ip']) in ipaddress.IPv4Network(result_estab[in_result+1]['i_su']):
                            specs_external_nic = result_estab[in_result+1]['i_su']
                     all_listen.setdefault('l_ip', result_estab[in_result+1]['l_ip'])
                     all_listen.setdefault('l_p', result_estab[in_result+1]['l_p'])
                     all_listen.setdefault('d_ip', result_estab[in_result+1]['d_ip'])
                     all_listen.setdefault('d_p', result_estab[in_result+1]['d_p'])
                     all_listen.setdefault('st_c', result_estab[in_result+1]['st_c'])
                     all_listen.setdefault('i_ni', result_estab[in_result+1]['i_ni'])
                     all_listen.setdefault('i_su', result_estab[in_result+1]['i_su'])
                     all_listen.setdefault('i_g', result_estab[in_result+1]['i_g'])
                     all_listen.setdefault('i_m', result_estab[in_result+1]['i_m'])
                     all_listen.setdefault('i_g_s', result_estab[in_result+1]['i_g_s'])
                     all_listen.setdefault('i_dg', result_estab[in_result+1]['i_dg'])
                     all_listen.setdefault('e_su', specs_external_nic)
                     all_listen.setdefault('ip_v', result_estab[in_result+1]['ip_v'])
                     all_listen.setdefault('pr', result_estab[in_result+1]['pr'])
                     all_listen.setdefault('p_n', result_estab[in_result+1]['p_n'])
                     all_listen.setdefault('pid', result_estab[in_result+1]['pid'])
                     isimult = isimult+1
                     cont_simul.setdefault(isimult, all_listen)
                     all_listen = {}
          save_in_file.save_in_file(cont_all,self.get_class_name(),cont_simul)
          return cont_simul
