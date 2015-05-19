#!/usr/bin/python

import argparse
import time
from Crypto.Hash import SHA256

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-k','--key', help='AES key.')
parser.add_argument('-s','--seed', help='AES seed.')
parser.add_argument('-n','--numbers', help='Desired quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

if args.key:
    key = args.key
else:
    key = b'85b5ac8190121c198185ce4945a187d3'

if args.seed:
    seed = args.seed
else:
    seed = b'a132adc5cf9e42f5644e4f3c85e997da'

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

salt = b'7b98bf3632a4f206f8dc4386d24066c5' # for PBKDF2
sha256 = SHA256.new(key)

# the actual ANSI X9.17 algorithm
for i in range(0, number):
    sha256.update(bytes(time.time()))
    temp = sha256.digest()
    sha256.update(sxor(seed, temp))
    out = sha256.digest()
    sha256.update(sxor(out, temp))
    seed = sha256.digest()
    print(int(out.encode('hex'), 16)/2**256.0)
