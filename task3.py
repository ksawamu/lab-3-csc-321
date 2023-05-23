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
    e = 65537
    d = pow(e, -1, ((p - 1) *(q - 1)))
    m0 = int(ASCIItoHEX("Hi Bob!"), 16)
    c = pow(m0, e, n)
    m = pow(c, d, n)
    m = bytearray.fromhex(hex(m)[2:]).decode()
    print(m)


    return True

print(diffie_hellman())