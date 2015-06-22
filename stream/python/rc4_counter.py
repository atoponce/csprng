#!/usr/bin/python

import argparse
import struct
import sys
import time
from Crypto.Cipher import ARC4
from Crypto.Hash import RIPEMD, SHA
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ARC4 in counter mode CSPRNG')
parser.add_argument('-b','--binary', help='Raw binary output.', action="store_true")
parser.add_argument('-k','--key', help='ARC4 key.')
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
number = 1

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16, 0)

if args.numbers:
    number = int(args.numbers)

arc4 = ARC4.new(key)
counter = int(time.time())

# the actual ANSI X9.17 algorithm
for i in xrange(0, number):
    out = arc4.encrypt(repr(counter).zfill(16))
    counter += 1
    if args.binary:
        sys.stdout.write(out)
    else:
        res = struct.unpack_from('QQ', out)
        print(res[0]*2**64+res[1])
