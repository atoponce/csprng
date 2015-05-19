#!/usr/bin/python

import getopt
import sys
import time
from Crypto.Cipher import AES
from Crypto.Protocol import KDF

def fread(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except IOError:
        # first initialization
        return b'QTKmMIVuO/LZpVKf'

def fwrite(path, seed):
    try:
        with open(path, 'w') as f:
            f.write(seed)
    except IOError:
        print("Cannot write seed to disk.")

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

# setup
path = '/var/tmp/ansi.seed'

# Input
salt = b'FFirhzZkFKARFduT' # for PBKDF2
K = b'My Super Secret Key' # user-input key
s = fread(path)

# env setup
key = KDF.PBKDF2(bytes(K), salt, 16)
aes = AES.new(key)

# the ANSI X9.17 algorithm
d = time.time()
D = KDF.PBKDF2(bytes(d), salt, 16)
t = aes.encrypt(D)
x = aes.encrypt(sxor(s,t))
print(int(x.encode('hex'), 16)/2**128.0)
s = aes.encrypt(sxor(x,t))
# end loop

# cleanup
fwrite(path, s)
