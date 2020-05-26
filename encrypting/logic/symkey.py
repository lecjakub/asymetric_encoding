class SymKey():
    def __init__(self,key,init_vector=None,counter=None):
        self.key = key
        self.init_vector = init_vector
        self.counter = counter

    @staticmethod
    def from_header(header):
        return SymKey(header.next_key,header.init_vector,header.counter)