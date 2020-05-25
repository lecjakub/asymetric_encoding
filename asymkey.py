import math
class AsymKey():
    def __init__(self,key_size=None,private_key=None,public_key=None):
        self.key_size = key_size
        self.private_key = private_key
        self.public_key = public_key

    def private_to_bytes(self):
        n, d, key_size = self.private_key

        result = key_size.to_bytes(4, 'little')
        n_size = math.ceil(n.bit_length() / 8)
        result += n_size.to_bytes(4, 'little')
        result += n.to_bytes(n_size, 'little')
        result += d.to_bytes(n_size, 'little')
        return result

    @staticmethod
    def private_from_file(file):
        key_size = int.from_bytes(file.read(4), 'little')
        n_size = int.from_bytes(file.read(4), 'little')
        n = int.from_bytes(file.read(n_size), 'little')
        d = int.from_bytes(file.read(n_size), 'little')
        return (n, d, key_size)
    
    def public_to_bytes(self):
        n,e,key_size = self.public_key

        result = key_size.to_bytes(4, 'little')
        n_size = math.ceil(n.bit_length() / 8)
        result += n_size.to_bytes(4, 'little')
        result += n.to_bytes(n_size, 'little')
        result += e.to_bytes(n_size, 'little')
        return result

    @staticmethod
    def public_from_file(file):
        key_size = int.from_bytes(file.read(4), 'little')
        n_size = int.from_bytes(file.read(4), 'little')
        n = int.from_bytes(file.read(n_size), 'little')
        e = int.from_bytes(file.read(n_size), 'little')
        return (n, e, key_size)