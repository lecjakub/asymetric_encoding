from encrypting.logic.algorithms import Algorithms
class Header():
    def __init__(self,final, next_alg, next_key, size_to_decode, file_name=None, plug_size=0,init_vector=None,counter=None):
        self.final = final

        if self.final:
            if file_name is None:
                raise ValueError()
            self.file_name = file_name
        self.plug_size = plug_size

        self.next_key = next_key
        self.next_alg = next_alg
        self.init_vector = init_vector
        self.counter = counter
        self.size_to_decode = size_to_decode
        
    
    @staticmethod
    def from_file(file):
        final = bool.from_bytes(file.read(1),'little')

        next_alg_val =int.from_bytes(file.read(4),'little')
        next_alg = Algorithms(next_alg_val)

        next_key_size = int.from_bytes(file.read(4),'little')
        next_key = file.read(next_key_size)

        iv_size = int.from_bytes(file.read(4),'little')
        init_vector = None
        if iv_size:
            init_vector = file.read(iv_size)

        counter_size = int.from_bytes(file.read(4),'little')
        counter = None
        if counter_size:
            counter = file.read(counter_size)


        file_name = None
        if final:
            file_name_size = int.from_bytes(file.read(4),'little')
            file_name = str(file.read(file_name_size),'ascii')
        
        plug_size = int.from_bytes(file.read(4),'little')
        
        size_to_decode = int.from_bytes(file.read(32),'little')
            # Is extension necessary?
            # file_ext_size = int.from_bytes(file.read(1),'little')
            # self.file_ext = str(file.read(file_ext_size),'ascii')

        return Header(final,next_alg,next_key,size_to_decode,file_name,plug_size,init_vector,counter)

    def to_bytes(self):
        # #writing data about final state
        result = self.final.to_bytes(1,'little')

        #writing data about next algorithm
        result += self.next_alg.value.to_bytes(4,'little')

        #writing data about next key
        result += len(self.next_key).to_bytes(4,'little')
        result += self.next_key

        #writing data about init vector
        if self.init_vector is None:
            result += int(0).to_bytes(4,'little')
        else:
            result += len(self.init_vector).to_bytes(4,'little')
            result += self.init_vector

        #writing data about counter
        if self.counter is None:
            result += int(0).to_bytes(4,'little')
        else:
            result += len(self.counter).to_bytes(4,'little')
            result += self.counter

        if self.final:
            #writing data about name
            result += len(self.file_name).to_bytes(4,'little')
            result += bytes(self.file_name,'ascii')
        
        result += self.plug_size.to_bytes(4,'little')
        #writing data about encrypted file size
        result += self.size_to_decode.to_bytes(32,'little')
        return result


