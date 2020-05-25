import sys
from rsa import Rsa
from ecb import Ecb
from cbc import Cbc
from ctr import Ctr
from algorithms import Algorithms
from asymkey import AsymKey
import core
ENCRYPT = True
DECRYPT = True

file_name = "message.t"
sym_key = Ctr.generate_key(32) 
print(sym_key.key)

asym_key = Rsa.generate_key(1024) 

encoded_file_data = core.encrypt_file(file_name,Algorithms.CTR,sym_key,Algorithms.RSA,asym_key)
#print(encoded_file_data)

encoded_file_name = "encoded.t"

encoded_file = open(encoded_file_name,"wb")
encoded_file.write(encoded_file_data)
encoded_file.close()

publicKey, privateKey = algorithms.get_keys(1024)

decoded_file_data, dfile_name = core.decrypt_file(encoded_file_name,asym_key)
#print(str(decoded_file_data,'ascii'))
decoded_file = open(dfile_name, "wb")
decoded_file.write(decoded_file_data)
decoded_file.close()
#encrypt_key, err = algorithm.encode(bytes(sym_key))

# print(encrypt_key,'\n')

# decrypt_key, err = algorithm.decode(encrypt_key)

# print(decrypt_key)