import hashlib
import binascii
class hash_log:
    def __init__(self,data):
        self.h_log = self.h_log_func(data)
    def h_log_func(self,password):
        hash_bytes = hashlib.pbkdf2_hmac('sha256', password, b'bad_sal@@@@@@@ssssssss@t', 10)
        hash_string = binascii.hexlify(hash_bytes).decode('utf-8')
        return binascii.hexlify(hash_string)

