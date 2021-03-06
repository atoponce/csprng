#!/usr/bin/python

import argparse
import struct
import sys
import time
from Crypto.Hash import RIPEMD, SHA
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ANSI x9.17 DRBG')
parser.add_argument('-b','--binary', help='Raw binary output.', action="store_true")
parser.add_argument('-k','--key', help='SHA-256 key.')
parser.add_argument('-s','--seed', help='Starting seed.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1,s2))

with open('/proc/interrupts','r') as f:
    data = f.read().replace('\n','')

d = RIPEMD.new(data)
ripemd = d.hexdigest()
d = SHA.new(data)
sha = d.hexdigest()
salt = sxor(sha, ripemd)
key = KDF.PBKDF2(sha, salt, 16, 0)
seed = KDF.PBKDF2(ripemd, salt, 16, 0)
number = 1

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 32, 0)

if args.seed:
    seed = KDF.PBKDF2(bytes(args.seed), salt, 32, 0)

if args.numbers:
    number = int(args.numbers)

# the actual ANSI X9.17 algorithm
for i in xrange(0, number):
    sha1 = SHA.new(key)
    sha1.update(bytes(time.time()))
    temp = sha1.digest()
    sha1.update(sxor(seed, temp))
    out = sha1.digest()
    sha1.update(sxor(out, temp))
    seed = sha1.digest()
    if args.binary:
        sys.stdout.write(out)
    else:
        res = struct.unpack_from('QQ', out)
        print(res[0]*2**64+res[1])
