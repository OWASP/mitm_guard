import datetime
import psutil
import netifaces
import datetime
from .connections import estab_conns,listen_conns,simul_conns,back_conns,arp_cache
from .nics import status_nics,available_nic,in_subnets
from .get_services import create_json,ret_cont_all,run_agent
#from .database import db_conn
class A:
    def __init__(self):
        #global cont_all
        cont_all = {}
        conns = sorted(psutil.net_connections())
        #print(conns)
        all_nics = netifaces.interfaces()
        #print(all_nics)
        status_nic = (status_nics.status_nics(all_nics,cont_all)).all_nics
        #print(status_nic)
        available_nics = (available_nic.available_nic(status_nic,all_nics,cont_all)).available_n
        #print(available_nics)
        self.inter_subnets = (in_subnets.in_subnets(available_nics,cont_all)).in_subs
        #estab_c = (estab_conns.estab_conns(conns,self.inter_subnets,cont_all)).estab_conn
        #print(estab_c)
        #listen_c = (listen_conns.listen_conns(conns,self.inter_subnets,cont_all)).lis_conn
        #print(listen_c)
        #simul_c = (simul_conns.simul_conns(estab_c, listen_c, self.inter_subnets,cont_all)).s_conns
        #print(simul_c)
        #back_c = (back_conns.back_conns(estab_c,listen_c,cont_all)).b_conns
        #print(back_c)
        self.arp_caches = (arp_cache.arp_cache(cont_all)).get_arp
        #print(arp_caches)
        #self.db = ((db_conn.db_conn()).db_server).alma_db
        self.id_agent = (run_agent.run_agent(self.inter_subnets)).ret
        self.return_cont_all = cont_all
        #print(self.return_json_cont_all)
