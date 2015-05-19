#!/usr/bin/python

import argparse
import sys
import time
from Crypto.Cipher import AES
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-k','--key', help='AES key.')
parser.add_argument('-s','--seed', help='AES seed.')
parser.add_argument('-n','--numbers', help='Desired quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

if args.key:
    K = args.key
else:
    K = b'11cf0edfc106350f9d81abe1538b3f20'

if args.seed:
    S = args.seed
else:
    S = b'11462794b14c20f6b0896bac3a921485'

salt = b'8bbb35cb1626f7c9ef291b29261acbf5' # for PBKDF2
key = KDF.PBKDF2(bytes(K), salt, 16)
seed = KDF.PBKDF2(bytes(S), salt, 16)
aes = AES.new(key)

if args.numbers:
    counter = args.numbers
else:
    counter = 1

# the actual ANSI X9.17 algorithm
for i in range(0, int(counter)):
    date = KDF.PBKDF2(bytes(time.time()), salt, 16)
    temp = aes.encrypt(date)
    out = aes.encrypt(sxor(seed,temp))
    seed = aes.encrypt(sxor(out,temp))
    print(int(out.encode('hex'), 16)/2**128.0)
