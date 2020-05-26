import sys
from encrypting.logic.rsa import Rsa
from encrypting.logic.ecb import Ecb
from encrypting.logic.cbc import Cbc
from encrypting.logic.ctr import Ctr
from encrypting.logic.algorithms import Algorithms
from encrypting.logic.asymkey import AsymKey
import encrypting.logic.core as core
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