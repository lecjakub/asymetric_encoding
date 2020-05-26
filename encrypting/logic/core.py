from encrypting.logic.algorithms import Algorithms
from encrypting.logic.header import Header
from encrypting.logic.symkey import SymKey
from encrypting.logic.asymkey import AsymKey
import os
from io import BytesIO


def encrypt_files(file_paths:list, public_key_path:str,alg_sym:str):
    with open(public_key_path, "rb") as pub_file:
        public_key = AsymKey.public_from_file(pub_file)
        asym_key = AsymKey(key_size=public_key[2], public_key=public_key)
        alg_dict = {
            'ecb': Algorithms.ECB,
            'cbc': Algorithms.CBC,
            'ctr': Algorithms.CTR,
        }
        alg1 = alg_dict[alg_sym]
        
        for file_path in file_paths:
            encrypted_data = __encrypt_file(file_path, alg1, alg2=Algorithms.RSA, key2=asym_key)
            with open(file_path+".enc",'wb') as enc_file:
                enc_file.write(encrypted_data)
            


def decrypt_files(file_paths:list, private_key_path:str):
    with open(private_key_path, "rb") as priv_file:
        private_key = AsymKey.private_from_file(priv_file)
        asym_key = AsymKey(key_size=private_key[2], private_key=private_key)
        for file_path in file_paths:
            decrypted_data, file_name = decrypt_file(file_path,asym_key)
            dir_path = os.path.dirname(file_path)
            with open(dir_path + "/" + file_name, 'wb') as dec_file:
                dec_file.write(decrypted_data)



def __encrypt_file(file_path, alg1:Algorithms,key1:SymKey=None, alg2:Algorithms=None, key2:AsymKey=None):
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

        if key1 is None:        
            key1 = alg1.get_type.generate_key(32)
        prime_alg:Algorithm = alg1.create(key1)
        encoded_file = prime_alg.encode(file.read() + plug)# ECB require that data is multiple of 16 so plug is used to extend data to nearest multiple of 16
        file_size += plug_size
        
        prime_header = Header(final=True,next_alg=alg1,next_key=key1.key,size_to_decode=file_size,file_name=file_name,plug_size=plug_size,init_vector=key1.init_vector,counter=key1.counter)

        if alg2 is not None:
            second_alg:Algorithm = alg2.create(key2)
            encoded_header = second_alg.encode(prime_header.to_bytes())
            second_header = Header(final=False,next_alg=alg2,next_key=b'',size_to_decode=len(encoded_header))

            encoded_file = second_header.to_bytes() + encoded_header + encoded_file
        else:
            encoded_file = prime_header.to_bytes() + encoded_file

        
        return encoded_file


def decrypt_file(file_path, key):
    with open(file_path,"rb") as file:
        outer_header = Header.from_file(file)
        outer_alg = outer_header.next_alg.create(key)

        inner_header_data, error = outer_alg.decode(file.read(outer_header.size_to_decode))
        if error:
            raise ArithmeticError

        inner_header = Header.from_file(BytesIO(inner_header_data))
        inner_key = SymKey.from_header(inner_header)
        inner_alg = inner_header.next_alg.create(inner_key)
        decrypted_file_data = inner_alg.decode(file.read())

        return decrypted_file_data[:-inner_header.plug_size] , inner_header.file_name

