import sys
from rsa import Rsa

ENCRYPT = True
DECRYPT = True

algorithm = Rsa(1024)
algorithm.get_keys()

sym_key = "haSLO123xd49494"

encrypt_key, err = algorithm.encode(map(ord,sym_key))

print(encrypt_key,'\n')

decrypt_key, err = algorithm.decode(encrypt_key)

print(decrypt_key)