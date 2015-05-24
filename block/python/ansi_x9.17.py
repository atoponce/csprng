#!/usr/bin/python

import argparse
import struct
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

salt = '8bbb35cb1626f7c9ef291b29261acbf5' # for PBKDF2
key = KDF.PBKDF2('11cf0edfc106350f9d81abe1538b3f20', salt, 16, 0)
seed = KDF.PBKDF2('11462794b14c20f6b0896bac3a921485', salt, 16, 0)

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16, 0)

if args.seed:
    seed = KDF.PBKDF2(bytes(args.seed), salt, 16, 0)

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

aes = AES.new(key)

# the actual ANSI X9.17 algorithm
for i in range(0, number):
    date = repr(time.time())
    temp = aes.encrypt(date.zfill(32))
    out = aes.encrypt(sxor(seed,temp))
    seed = aes.encrypt(sxor(out,temp))
    res = struct.unpack('QQ', out)
    print res[0]+res[1]*2**64
