from algorithms import Algorithms
from algorithm import Algorithm
from key import Key
from header import Header
import os

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
            plug +=b'0'

        prime_alg:Algorithm = alg1.create(key1)
        encoded_file, prime_key = prime_alg.encode(file.read() + plug)
        
        prime_header = Header(final=True,next_alg=alg1,next_key=prime_key,size_to_decode=file_size,file_name=file_name)

        if alg2 is not None:
            second_alg:Algorithm = alg2.create(key2)
            second_alg.generate_keys()
            encoded_header, second_key = second_alg.encode(prime_header.to_bytes())
            second_header = Header(final=False,next_alg=alg2,next_key=b'',size_to_decode=len(encoded_header))

            encoded_file = second_header.to_bytes() + encoded_header + encoded_file
        else:
            encoded_file = prime_header.to_bytes() + encoded_file

        return encoded_file


    

