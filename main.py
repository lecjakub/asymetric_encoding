import core
import algorithms
import sys

ENCRYPT = True
DECRYPT = True

input_ = sys.argv[1]
output = sys.argv[2]


publicKey, privateKey = algorithms.get_keys(32)


print(publicKey)
print(privateKey)

if ENCRYPT:
    core.encrypt_file(input_,output,publicKey)

if DECRYPT:
    core.decrypt_file(output,input_ + 'decoded.txt',privateKey)