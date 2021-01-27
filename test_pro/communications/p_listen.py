import socket
import sys
class lis_main():
    def port_listen(self):
        host = '0.0.0.0'
        port = 2882
        address = (host, port)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(address)
        server_socket.listen(5)
        return server_socket
"""
        while True:
            conn, address = server_socket.accept()
            conn
            val = str(action)
            sender = conn.send(val.encode())
            output = conn.recv(2048).decode();
            print(output)
"""
