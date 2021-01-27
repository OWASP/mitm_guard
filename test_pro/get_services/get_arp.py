class get_arp:
    def __init__(self):
        self.g_arp = self.get_arp_cache()
    def get_arp_cache(self):
        with open("/proc/net/arp") as f:
            content = f.readlines()
            del content[0]
            arp_dic = {}
            vvv = {}
            content_new = None
            iii = 1
            for aaa in range(len(content)):
                content_new = " ".join(content[aaa].split())
                vvv.setdefault('ip', content_new.split(" ")[0])
                vvv.setdefault('mac', content_new.split(" ")[3])
                vvv.setdefault('nic', content_new.split(" ")[5])
                arp_dic.setdefault(iii,vvv)
                vvv = {}
                iii = iii+1
            return arp_dic
