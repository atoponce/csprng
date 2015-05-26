#!/usr/bin/node

var BigNumber = require('bignumber');
var crypto = require('crypto');
var stdio = require('stdio');

var opts = stdio.getopt({
    'binary': {key: 'b', args: 0, description: 'Raw binary output.'},
    'key': {key: 'k', args: 1, description: 'RC4 key.'},
    'numbers': {key: 'n', args: 1, description: 'Quantity of random numbers.'}
});

function encrypt(s, k) {
    var rc4 = crypto.createCipher('rc4', k);
    return rc4.update(s);
}

var salt = 'f1af459e9cf4dd33168d1bcfdeea03a5'; // for pbkdf2
var key = crypto.pbkdf2Sync('3049074005466cb6615601e698b06540', salt, 0, 16);
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
