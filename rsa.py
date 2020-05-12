import math
import random
import sympy as sy

# lower common multiplier
def lcm(a, b):
    return int(a*b / math.gcd(a, b))


def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


#  ( a * x ) % m == 1


def rsa(p, q):
    n = p * q
    phi = lcm(p - 1, q - 1)

    shuffleArray = list(range(2, phi))
    random.shuffle(shuffleArray)

    for e in shuffleArray:  
        if math.gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)

    print("Klucz publiczny : (" + str(n) + "," + str(e) + ")")
    print("Klucz prywatny : (" + str(n) + "," + str(d) + ")")


p = sy.randprime(1e2, 1e4)
q = sy.randprime(1e2, 1e4)

while q == p:
    q = sy.randprime(1e4, 1e8)

rsa(p, q)



