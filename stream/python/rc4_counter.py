#!/usr/bin/python

import argparse
import struct
import sys
import time
from Crypto.Cipher import ARC4
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='ARC4 in counter mode CSPRNG')
parser.add_argument('-b','--binary', help='Raw binary output.', action="store_true")
parser.add_argument('-k','--key', help='ARC4 key.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

salt = '819f5b3df9d515a807d0a5418d28a750' # for PBKDF2
key = KDF.PBKDF2('f3963721d2c024efd8a5eea90233d2a9', salt, 16, 0)

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16, 0)

if args.numbers:
    number = int(args.numbers)
else:
    number = 1

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
