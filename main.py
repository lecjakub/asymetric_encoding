import sys
from rsa import Rsa
from algorithms import Algorithms
import core
ENCRYPT = True
DECRYPT = True

alen = Algorithms.RSA
algorithm = alen.create(1024)
algorithm.generate_keys()

file_name = "message.t"
sym_key = b'1234567890123456'
print(len(sym_key))

encoded_file = core.encrypt_file(file_name,Algorithms.ECB,sym_key,Algorithms.RSA,32)
print(encoded_file)
#encrypt_key, err = algorithm.encode(bytes(sym_key))

# print(encrypt_key,'\n')

# decrypt_key, err = algorithm.decode(encrypt_key)

# print(decrypt_key)