#!/usr/bin/node

var BigNumber = require('bignumber');
var crypto = require('crypto');
var stdio = require('stdio');

var opts = stdio.getopt({
    'key': {key: 'k', args: 1, description: 'RC4 key.'},
    'seed': {key: 's', args: 1, description: 'Starting seed.'},
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

var salt = 'f1af459e9cf4dd33168d1bcfdeea03a5'; // for pbkdf2
var key = crypto.pbkdf2Sync('3049074005466cb6615601e698b06540', salt, 0, 16);
var seed = new Buffer('01e29845c6a7907487e6df778c18d649', 'hex');
var number = 1;

if(opts.key) key = crypto.pbkdf2Sync(opts.key, salt, 0, 16);
if(opts.seed) seed = crypto.pbkdf2Sync(opts.seed, salt, 0, 16);
if(opts.numbers) number = opts.numbers;

// Almost never return exponential notation
BigNumber.config({ EXPONENTIAL_AT: 1e+9 });

// Start nanoseconds benchmarking
var startTime = process.hrtime();

for (var i=0; i<number; i++) {
    var date = crypto.pbkdf2Sync(Date.now()+process.hrtime(startTime), salt, 0, 16);
    var temp = new Buffer(encrypt(date, key));
    var out = new Buffer(encrypt(xor(seed, temp), key));
    seed = new Buffer(encrypt(xor(out, temp), key));
    console.log(new BigNumber(out.toString('hex'), 16).toString());
}
