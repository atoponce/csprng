#!/usr/bin/python

import argparse
import struct
import sys
import time
from Crypto.Cipher import AES
from Crypto.Protocol import KDF

parser = argparse.ArgumentParser(description='AES in counter mode CSPRNG')
parser.add_argument('-b','--binary', help='Raw binary output.', action="store_true")
parser.add_argument('-k','--key', help='AES key.')
parser.add_argument('-n','--numbers', help='Quantity of random numbers.')
args = parser.parse_args()

salt = 'c7575a194b575ee2f5001483515e3d74' # for PBKDF2
key = KDF.PBKDF2('0a7b92cb8bb4392ed08f896173a02326', salt, 16, 0)
number = 1

if args.key:
    key = KDF.PBKDF2(bytes(args.key), salt, 16, 0)

if args.numbers:
    number = int(args.numbers)

aes = AES.new(key)
counter = int(time.time())

# AES in counter mode
for i in xrange(0, number):
    out = aes.encrypt(repr(counter).zfill(16))
    counter += 1
    if args.binary:
        sys.stdout.write(out)
    else:
        res = struct.unpack('QQ', out)
        print(res[0]*2**64+res[1])
