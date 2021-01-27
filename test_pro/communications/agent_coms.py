import socket
import sys
class agent_coms:
    def __init__(self, ip, port):
        self.agent_com = self.relation(ip, port)
    def relation(self, ip, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
        return client_socket
#        while True:
#            self.get_p = client_socket.recv(2048).decode()
            #print(self.get_p)
"""
            self.result = get_p.split(".")
            self.p = result[0]
            self.proc_action = self.result[1]
            if self.proc_action == '0':
                self.act.all_actions(self.p_num)
"""
"""
            else:
                self.client_socket.send(data.encode())
                self.aaa = client_socket.recv(2048)123.decode()
                if self.aaa == "closed":
                    print(self.aaa)
                    self.client_socket.close()
                    sys.exit("Shutting down.")
"""
