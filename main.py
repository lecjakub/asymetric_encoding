import sys
from rsa import Rsa
from algorithms import Algorithms
from asymkey import AsymKey
import core
ENCRYPT = True
DECRYPT = True

alen = Algorithms.RSA
algorithm = alen.create(1024)
algorithm.get_keys()

file_name = "message.t"
sym_key = b'1234567890123456'
print(len(sym_key))

asym_key = Rsa.generate_key(32)

encoded_file_data = core.encrypt_file(file_name,Algorithms.ECB,sym_key,Algorithms.RSA,asym_key)
print(encoded_file_data)
encoded_file_name = "encoded.t"
encoded_file = open(encoded_file_name,"wb")
encoded_file.write(encoded_file_data)
encoded_file.close()


decoded_file = core.decrypt_file(encoded_file_name,asym_key)
print(str(decoded_file,'ascii'))
#encrypt_key, err = algorithm.encode(bytes(sym_key))

# print(encrypt_key,'\n')

# decrypt_key, err = algorithm.decode(encrypt_key)

# print(decrypt_key)