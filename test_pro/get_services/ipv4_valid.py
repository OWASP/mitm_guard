import socket
class ipv4_valid():
    def __init__(self, address):
        self.ip_val = self.ip_valid(address)
    def ip_valid(self,add):
      try:
          socket.inet_pton(socket.AF_INET, add)
      except AttributeError:  # no inet_pton here, sorry
          try:
              socket.inet_aton(add)
          except socket.error:
              return False
          return add.count('.') == 3
      except socket.error:  # not a valid address
          return False
      return True
