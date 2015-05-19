#!/usr/bin/python

import argparse
import time
from Crypto.Cipher import ARC4
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-k','--key', help='AES key.')
parser.add_argument('-s','--seed', help='AES seed.')
parser.add_argument('-n','--numbers', help='Desired quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

salt = b'25f32d809f5a3b0a5c54650547ec67c6' # for PBKDF2

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16)
else:
    key = KDF.PBKDF2(b'11cf0edfc106350f9d81abe1538b3f20', salt, 16)

if args.seed:
    seed = KDF.PBKDF2(bytes(args.seed), salt, 16)
else:
    seed = KDF.PBKDF2(b'807f0b5ca6725ad073a37f5abaf8de39', salt, 16)

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

arc4 = ARC4.new(key)

# the actual ANSI X9.17 algorithm
for i in range(0, number):
    date = KDF.PBKDF2(bytes(time.time()), salt, 16)
    temp = arc4.encrypt(date)
    out = arc4.encrypt(sxor(seed, temp))
    seed = arc4.encrypt(sxor(out, temp))
    print(int(out.encode('hex'), 16)/2**128.0)
    