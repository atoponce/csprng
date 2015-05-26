#!/usr/bin/python

import argparse
import struct
import sys
import time
from Crypto.Hash import SHA
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='SHA-1 in counter mode CSPRNG')
parser.add_argument('-b','--binary', help='Raw binary output.', action="store_true")
parser.add_argument('-k','--key', help='SHA-1 key.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

salt = '957954e4e3cc45e5049f20bfad8a58f2' # for PBKDF2
key = KDF.PBKDF2('faf72df86670f51512482d9ff0fb62f3', salt, 16, 0)
number = 1

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16, 0)

if args.numbers:
    number = int(args.numbers)

counter = int(time.time())

# SHA-1 in counter mode
for i in xrange(0, number):
    sha1 = SHA.new(key)
    sha1.update(bytes(counter))
    out = sha1.digest()
    counter += 1
    if args.binary:
        sys.stdout.write(out)
    else:
        res = struct.unpack_from('QQ', out)
        print(res[0]*2**64+res[1])
