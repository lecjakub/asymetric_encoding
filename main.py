import sympy as sy
import core
import algorithms

ENCRYPT = True
DECRYPT = False

p = sy.randprime(1e2, 1e3)
q = sy.randprime(1e2, 1e3)
while q == p:
    q = sy.randprime(1e2, 1e4)

publicKey, privateKey = algorithms.get_keys(p, q)

print(publicKey)
print(privateKey)


if ENCRYPT:
    core.encrypt_file("dupa.txt","dupa_encoded.txt",publicKey)

if DECRYPT:
    core.decrypt_file("dupa_encoded.txt","dupa_decoded.txt",privateKey)