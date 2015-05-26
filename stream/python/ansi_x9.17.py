#!/usr/bin/python

import argparse
import struct
import sys
import time
from Crypto.Cipher import ARC4
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-b','--binary', help='Raw binary output.', action="store_true")
parser.add_argument('-k','--key', help='ARC4 key.')
parser.add_argument('-s','--seed', help='Starting seed.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

salt = '25f32d809f5a3b0a5c54650547ec67c6' # for PBKDF2
key = KDF.PBKDF2('11cf0edfc106350f9d81abe1538b3f20', salt, 16, 0)
seed = KDF.PBKDF2('807f0b5ca6725ad073a37f5abaf8de39', salt, 16, 0)

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16, 0)

if args.seed:
    seed = KDF.PBKDF2(bytes(args.seed), salt, 16, 0)

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

arc4 = ARC4.new(key)

# the actual ANSI X9.17 algorithm
for i in xrange(0, number):
    date = repr(time.time())
    temp = arc4.encrypt(date.zfill(32))
    out = arc4.encrypt(sxor(seed, temp))
    seed = arc4.encrypt(sxor(out, temp))
    if args.binary:
        sys.stdout.write(out)
    else:
        res = struct.unpack_from('QQ', out)
        print(res[0]*2**64+res[1])
