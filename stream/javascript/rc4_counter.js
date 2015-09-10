#!/usr/bin/node

var BigNumber = require('bignumber.js');
var crypto = require('crypto');
var fs = require('fs');
var stdio = require('stdio');

var opts = stdio.getopt({
    'binary': {key: 'b', args: 0, description: 'Raw binary output.'},
    'key': {key: 'k', args: 1, description: 'RC4 key.'},
    'numbers': {key: 'n', args: 1, description: 'Quantity of random numbers.'}
});

function xor(s1, s2) {
    s1 = new Buffer(s1);
    s2 = new Buffer(s2);
    var xor = [];
    for (var i=0; i<s1.length; i++) {
        xor.push(s1[i]^s2[i]);
    }
    return new Buffer(xor);
}

function encrypt(s, k) {
    var rc4 = crypto.createCipher('rc4', k);
    return rc4.update(s);
}

var data = fs.readFileSync('/proc/interrupts').toString();
var d = crypto.createHash('sha1');
var sha = d.update(data).digest();
var d = crypto.createHash('ripemd160');
var ripemd = d.update(data).digest();
var salt = xor(sha, ripemd);
var key = crypto.pbkdf2Sync(sha, salt, 0, 16);
var number = 1;

if(opts.key) key = crypto.pbkdf2Sync(opts.key, salt, 0, 16);
if(opts.numbers) number = opts.numbers;

// Almost never return exponential notation
BigNumber.config({ EXPONENTIAL_AT: 1e+9 });

// Start nanoseconds benchmarking
var startTime = process.hrtime();
var counter = Date.now();

for (var i=0; i<number; i++) {
    var ctr = crypto.pbkdf2Sync(counter+process.hrtime(startTime), salt, 0, 16);
    var out = new Buffer(encrypt(ctr, key));
    counter++;
    if(opts.binary) process.stdout.write(out);
    else console.log(new BigNumber(out.toString('hex'), 16).toString());
}
