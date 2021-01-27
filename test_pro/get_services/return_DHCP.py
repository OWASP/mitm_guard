from . import create_json
class return_DHCP:
    def __init__(self):
        self.ret = self.ret_dhcp()
    def ret_dhcp(self):
        store_DHCP ={}
        store_DHCP.setdefault("ip"," ")
        store_DHCP.setdefault("mac"," ")
        all_json_DHCP_agent = (create_json.create_json(store_DHCP)).ret_json
        return all_json_DHCP_agent
