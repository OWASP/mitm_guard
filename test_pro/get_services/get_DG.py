from . import local_net_conns
class get_DG:
    def __init__(self):
        self.g_dg = self.get_DG_per_nic()
    def get_DG_per_nic(self):
      get_status = local_net_conns.in_subnets.in_subs
      eee = {}
      iii = 1
      gw = []
      new_eee = {}
      for i in range(len(get_status)):
        gw.append(get_status[i][2])
      return gw