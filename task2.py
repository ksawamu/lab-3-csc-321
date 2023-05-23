from random import *
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Random import get_random_bytes

def diffie_hellman():
    p = int.from_bytes(b"\xB1\x0B\x8F\x96\xA0\x80\xE0\x1D\xDE\x92\xDE\x5E\xAE\x5D\x54\xEC\x52\xC9\x9F\xBC\xFB\x06\xA3\xC6\x9A\x6A\x9D\xCA\x52\xD2\x3B\x61\x60\x73\xE2\x86\x75\xA2\x3D\x18\x98\x38\xEF\x1E\x2E\xE6\x52\xC0\x13\xEC\xB4\xAE\xA9\x06\x11\x23\x24\x97\x5C\x3C\xD4\x9B\x83\xBF\xAC\xCB\xDD\x7D\x90\xC4\xBD\x70\x98\x48\x8E\x9C\x21\x9A\x73\x72\x4E\xFF\xD6\xFA\xE5\x64\x47\x38\xFA\xA3\x1A\x4F\xF5\x5B\xCC\xC0\xA1\x51\xAF\x5F\x0D\xC8\xB4\xBD\x45\xBF\x37\xDF\x36\x5C\x1A\x65\xE6\x8C\xFD\xA7\x6D\x4D\xA7\x08\xDF\x1F\xB2\xBC\x2E\x4A\x43\x71", byteorder="big")
    g = p - 1#int.from_bytes(b"\xA4\xD1\xCB\xD5\xC3\xFD\x34\x12\x67\x65\xA4\x42\xEF\xB9\x99\x05\xF8\x10\x4D\xD2\x58\xAC\x50\x7F\xD6\x40\x6C\xFF\x14\x26\x6D\x31\x26\x6F\xEA\x1E\x5C\x41\x56\x4B\x77\x7E\x69\x0F\x55\x04\xF2\x13\x16\x02\x17\xB4\xB0\x1B\x88\x6A\x5E\x91\x54\x7F\x9E\x27\x49\xF4\xD7\xFB\xD7\xD3\xB9\xA9\x2E\xE1\x90\x9D\x0D\x22\x63\xF8\x0A\x76\xA6\xA2\x4C\x08\x7A\x09\x1F\x53\x1D\xBF\x0A\x01\x69\xB6\xA2\x8A\xD6\x62\xA4\xD1\x8E\x73\xAF\xA3\x2D\x77\x9D\x59\x18\xD0\x8B\xC8\x85\x8F\x4D\xCE\xF9\x7C\x2A\x24\x85\x5E\x6E\xEB\x22\xB3\xB2\xE5", byteorder="big")
   
    
    a = randint(1, p -1)
    b = randint(1, p -1)
    a_public_message = pow(g, a, p)
    b_public_message = pow(g, b, p)


    b_symmetric_from_a = pow(a_public_message, b, p)
    a_symmetric_from_b = pow(b_public_message, a, p)

    k = hashlib.sha256(str(b_symmetric_from_a).encode()).digest()[:16]
    print(hashlib.sha256(str(b_symmetric_from_a).encode()))
    iv = get_random_bytes(16)
    cipher = AES.new(k, AES.MODE_CBC, iv)

    m0 = "Hi Bob!"
    m1 = "Hi Alice!"

    c0 = cipher.encrypt(pad(str(m0).encode(), AES.block_size, style='pkcs7'))
    c1 = cipher.encrypt(pad(str(m1).encode(), AES.block_size, style='pkcs7'))

    cipher = AES.new(k, AES.MODE_CBC, iv)

    d0 = unpad(cipher.decrypt(c0), AES.block_size)
    d1 = unpad(cipher.decrypt(c1), AES.block_size)

    print(d0)
    print(d1)
    return b_symmetric_from_a == a_symmetric_from_b

print(diffie_hellman())