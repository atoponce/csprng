#!/usr/bin/python

import argparse
import time
from Crypto.Cipher import AES
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-k','--key', help='AES key.')
parser.add_argument('-s','--seed', help='Starting seed.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

salt = b'8bbb35cb1626f7c9ef291b29261acbf5' # for PBKDF2

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16)
else:
    key = KDF.PBKDF2(b'11cf0edfc106350f9d81abe1538b3f20', salt, 16)

if args.seed:
    seed = KDF.PBKDF2(bytes(args.seed), salt, 16)
else:
    seed = KDF.PBKDF2(b'11462794b14c20f6b0896bac3a921485', salt, 16)

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

aes = AES.new(key)

# the actual ANSI X9.17 algorithm
for i in range(0, number):
    date = KDF.PBKDF2(bytes(time.time()), salt, 16)
    temp = aes.encrypt(date)
    out = aes.encrypt(sxor(seed,temp))
    seed = aes.encrypt(sxor(out,temp))
    print(int(out.encode('hex'), 16)/2**128.0)
