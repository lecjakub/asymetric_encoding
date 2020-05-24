from algorithms import Algorithms
from utils import bytes_needed
class Header():
    def __init__(self,final, next_alg, next_key, size_to_decode, file_name=None):
        self.final = final

        if self.final:
            self.file_name = file_name

        self.next_key = next_key
        self.next_alg = next_alg
        self.size_to_decode = size_to_decode
        
    
    @staticmethod
    def from_file(file):
        final = bool.from_bytes(file.read(1),'little')

        next_alg_val =int.from_bytes(file.read(4),'little')
        next_alg = Algorithms(next_alg_val)

        next_key_size = int.from_bytes(file.read(4),'little')
        next_key = file.read(next_key_size)

        if final:
            file_name_size = int.from_bytes(file.read(4),'little')
            file_name = str(file.read(file_name_size),'ascii')
        
        size_to_decode = int.from_bytes(file.read(32),'little')
            # Is extension necessary?
            # file_ext_size = int.from_bytes(file.read(1),'little')
            # self.file_ext = str(file.read(file_ext_size),'ascii')

        return Header(final,next_alg,next_key,size_to_decode,file_name)

    def to_bytes(self):
        # #writing data about final state
        result = self.final.to_bytes(1,'little')

        #writing data about next algorithm
        result += self.next_alg.value.to_bytes(4,'little')

        #writing data about next key
        result += len(self.next_key).to_bytes(4,'little')
        result += self.next_key#.to_bytes(len(self.next_key),'little')

        if self.final:
            #writing data about name
            result += len(self.file_name).to_bytes(4,'little')
            result += bytes(self.file_name,'ascii') + result
        
        #writing data about encrypted file size
        result += self.size_to_decode.to_bytes(32,'little')
        return result


