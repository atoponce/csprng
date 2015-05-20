#!/usr/bin/python

import argparse
import time
from Crypto.Hash import SHA256
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-k','--key', help='SHA-256 key.')
parser.add_argument('-s','--seed', help='Starting seed.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

salt = '1f787c00c11fadf15d744ca97c64b640' # for PBKDF2

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 32)
else:
    key = KDF.PBKDF2('85b5ac8190121c198185ce4945a187d3', salt, 32)

if args.seed:
    seed = KDF.PBKDF2(bytes(args.seed), salt, 32)
else:
    seed = KDF.PBKDF2('a132adc5cf9e42f5644e4f3c85e997da', salt, 32)

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

# the actual ANSI X9.17 algorithm
for i in range(0, number):
    sha256 = SHA256.new(key)
    sha256.update(bytes(time.time()))
    temp = sha256.digest()
    sha256.update(sxor(seed, temp))
    out = sha256.digest()
    sha256.update(sxor(out, temp))
    seed = sha256.digest()
    print(int(out.encode('hex'), 16)%2**128)
