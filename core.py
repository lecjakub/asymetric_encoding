from algorithms import Algorithms
from algorithm import Algorithm
from key import Key
from header import Header
import os
from io import BytesIO

def encrypt_file(file_path, alg1:Algorithms,key1=None, alg2:Algorithms=None, key2=None):
    #alg1 - algorithm used to encode file
    #key1 - key for algorithm1
    #alg2 - optional second algorithm used to encode key for alg1
    #key2 - if alg2 is specified, key2 is key for algorithm2

    with open(file_path,"rb") as file:
        file_name = os.path.basename(file_path)
        file_size = os.stat(file_path).st_size
        plug_size = (16 - (file_size % 16)) % 16
        plug = b''
        for _ in range(plug_size):
            plug +=b'\0'

        prime_alg:Algorithm = alg1.create(key1)
        encoded_file, prime_key = prime_alg.encode(file.read() + plug)# ECB require that data is multiple of 16 so plug is used to extend data to nearest multiple of 16
        file_size += plug_size
        
        prime_header = Header(final=True,next_alg=alg1,next_key=prime_key,size_to_decode=file_size,file_name=file_name)

        if alg2 is not None:
            second_alg:Algorithm = alg2.create(key2)
            encoded_header, second_key = second_alg.encode(prime_header.to_bytes())
            second_header = Header(final=False,next_alg=alg2,next_key=b'',size_to_decode=len(encoded_header))

            encoded_file = second_header.to_bytes() + encoded_header + encoded_file
        else:
            encoded_file = prime_header.to_bytes() + encoded_file

        
        return encoded_file, plug_size


def decrypt_file(file_path, key):
    with open(file_path,"rb") as file:
        outer_header = Header.from_file(file)
        print(file.tell())
        outer_alg = outer_header.next_alg.create(key)

        inner_header_data, error = outer_alg.decode(file.read(outer_header.size_to_decode))
        if error:
            raise ArithmeticError

        inner_header = Header.from_file(BytesIO(inner_header_data))

        inner_alg = inner_header.next_alg.create(inner_header.next_key)
        decrypted_file_data = inner_alg.decode(file.read())

        return decrypted_file_data , inner_header.file_name + "d"
        # decrypted_file = open(inner_header.file_name,"wb")
        # decrypted_file.write(decrypted_file_data)
        # decrypted_file.close()


    

