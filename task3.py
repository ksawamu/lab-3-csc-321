from random import *
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime
#from math import *

# Source: https://www.geeksforgeeks.org/convert-a-string-to-hexadecimal-ascii-values/
# function to convert ASCII to HEX
def ASCIItoHEX(ascii):
 
    # Initialize final String
    hexa = ""
 
    # Make a loop to iterate through
    # every character of ascii string
    for i in range(len(ascii)):
 
        # take a char from
        # position i of string
        ch = ascii[i]
 
        # cast char to integer and
        # find its ascii value
        in1 = ord(ch)
   
        # change this ascii value
        # integer to hexadecimal value
        part = hex(in1).lstrip("0x").rstrip("L")
 
        # add this hexadecimal value
        # to final string.
        hexa += part
 
    # return the final string hex
    return hexa

def diffie_hellman():
    p = getPrime(2048)
    q = getPrime(2048)
    n = p * q
    M = "some random message"
    e = 65537
    numBits = choice([2048, 512, 1024])
    k = str(getPrime(numBits)).encode('utf-8')[:16]
    d = pow(e, -1, ((p - 1) *(q - 1)))
    print(d)



    # do encryption - one line with the pow
    C = pow(M, e, n)
    # do decryption
    dM = pow(C, d, n)

    print("PU = ")
    print((e, n))
    print("PR = ")
    print((d, n))
    print(k)
    #multInv = 1/k

    m0 = int(ASCIItoHEX("Hi Bob!"), 16)
   # m1 = "Hi Alice!".encode('utf-8').hex()
    print(m0)
    print("m")
    print(type(m0))
    print("d")
    print(d)
    print(type(d))
    print("n")
    print(type(n))
    print("e")
    print(type(e))

    #print(m1)

    c = pow(m0, e, n)
    print("c")
    print(c)
    m = pow(c, d) % n
    print("m")
    print(m)


    a = randint(1, p -1)
    b = randint(1, p -1)


    return "=^x^="

print(diffie_hellman())