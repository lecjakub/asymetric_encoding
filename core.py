from algorithms import Algorythms
from algorithm import Algorithm
from key import Key
def encrypt_file(file, alg1:Algorythms,key1:Key=None, alg2:Algorythms=None, key2:Key=None):
    #alg1 - algorithm used to encode file
    #key1 - key for algorithm1
    #alg2 - optional second algorithm used to encode key for alg1
    #key2 - if alg2 is specified, key2 is key for algorithm2
    
    prime_alg:Algorithm = alg1.ctor()(key1)
    encoded_file, prime_header, prime_key = prime_alg.encode(file)

    if alg2 is not None:
        second_alg:Algorithm = alg2.ctor()(key2)
        encoded_header, second_header = second_alg.encode(prime_header,prime_key)

        encoded_file = second_header + encoded_header + encoded_file
    else:
        encoded_file = prime_header + encoded_file

    return encoded_file


    

