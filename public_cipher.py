from random import *
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib


def diffie_hellman():
    g = 35
    p = 5
    a = randint(1, p -1)
    b = randint(1, p -1)
    a_public_message = pow(g, a, p)
    b_public_message = pow(g, b, p)
    bs_from_a = pow(a_public_message, b) % p
    as_from_b = pow(b_public_message, a) % p

    k = hashlib.sha256(str(bs_from_a).encode()).digest()[:16]
    cipher = AES.new(k, AES.MODE_CBC)

    m0 = "Hi Bob!"
    m1 = "Hi Alice!"

    c0 = cipher.encrypt(pad(str(m0).encode(), AES.block_size, style='pkcs7'))
    c1 = cipher.encrypt(pad(str(m1).encode(), AES.block_size, style='pkcs7'))

    print(c0)
    print(c1)
    return (bs_from_a == as_from_b)

print(diffie_hellman())