import os
import json
import datetime
import subprocess
from . import return_DG_MAC,return_DNS,return_DHCP,create_json,write_line
class run_agent:
    def __init__(self,ip_add):
        self.ret = self.r_agent(ip_add)
    def r_agent(self,ip_add):
        #def exist_u(uuid):
        #    result = db.agents_info.find_one({"UUID":uuid})
        #   if result is None:
        #       return 0
        #    else:
        #        return result["_id"]
        loc_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = str('/'+loc_path.split('/')[1])+str('/'+loc_path.split('/')[2])+"/.run_agent/"
        data = {}
        ips = {}
        get_dg = (return_DG_MAC.return_DG_MAC()).ret
        get_dns = (return_DNS.return_DNS(ip_add)).ret
        get_dhcp = (return_DHCP.return_DHCP()).ret
        exist_dir = os.path.isdir(dir_path)
        exist_file = os.path.isfile(dir_path+".setting")
        system_uuid = subprocess.Popen(['dmidecode','-s','system-uuid'], stdout=subprocess.PIPE)
        output, err = system_uuid.communicate()
        uuid = str(output).split("'")[1].split("\\")[0]
        #id_exist_uuid = exist_u(uuid)
        setup_date = datetime.datetime.now()
        if not exist_dir:
            os.system('mkdir '+dir_path)
        if not exist_file:
            os.system('touch '+dir_path+".setting")
            id_setting = 1 #db.agents_info.count()+1
            #['ens33', '192.168.100.0/24', '192.168.100.1', '00:0c:29:da:0e:f2', True, '192.168.100.1', '192.168.100.219']
            #agent_details = {"_id":id_setting,"UUID":uuid,"IP":ip_add[0][6],"DG":get_dg,"DNS":get_dns,"DHCP":get_dhcp}
            #json_agent_detailst = create_json.json_dic.ret_json(agent_details)
            #db.agents_info.insert(json_agent_detailst)
            #for i in range(len(ip_add.keys())):
            #   data.setdefault('IP'+i+1, str(ip_add[i+1][6]))
            for n in range(len(ip_add)):
                ips.setdefault(str(n+1), str(ip_add[n][6]))
            data.setdefault('IP', ips)
            #data.setdefault('IP', str(ip_add[0][6]))
            data.setdefault('DG', get_dg)
            data.setdefault('DNS', get_dns)
            data.setdefault('DHCP', get_dhcp)
            data.setdefault('UUID', str(uuid))
            data.setdefault('ID_Con', str(id_setting))
            data.setdefault('Port', str(80))
            data.setdefault('Setup_Date', str(setup_date))
            with open(dir_path+'.setting', 'w') as outfile:
                json.dump(data, outfile)
        setting = open(dir_path+'.setting', 'r+')
        return setting.readlines()
        setting.close()