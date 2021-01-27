from . import connections
from . import nics
from .. import ipv4_valid as ip_valid
from .. import all_ps
import netifaces

import psutil
from netaddr import IPAddress
global cont_all_local
cont_all_local = {}
conns = sorted(psutil.net_connections())
all_nics = netifaces.interfaces()
status_nics = nics.status_nics.status_nics(all_nics,cont_all_local)
available_nic = nics.available_nic.available_nic(status_nics.all_nics,all_nics,cont_all_local)
#print(available_nic.available_n)
in_subnets = nics.in_subnets.in_subnets(available_nic.available_n,cont_all_local)
#print(in_subnets.in_subs)
#estab_conns = connections.estab_conns.estab_conns(conns,in_subnets.in_subs,cont_all_local,ip_valid,all_ps)
#print(estab_conns.estab_conn)
#listen_conns = connections.listen_conns.listen_conns(conns,in_subnets.in_subs,cont_all_local,ip_valid,all_ps)
#print(listen_conns.lis_conn)
#simul_conns = connections.simul_conns.simul_conns(estab_conns.estab_conn, listen_conns.lis_conn, in_subnets.in_subs,cont_all_local)
#print(simul_conns.simultaneously_conns)
#ack_conns= connections.back_conns.back_conns(estab_conns.estab_conn, listen_conns.lis_conn,cont_all_local)
#print(back_conns.back_connections)
arp_cache= connections.arp_cache.arp_cache(cont_all_local)
#print(arp_cache.get_arp)