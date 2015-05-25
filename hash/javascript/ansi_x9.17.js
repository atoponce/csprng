#!/usr/bin/node

var BigNumber = require('bignumber');
var crypto = require('crypto');
var stdio = require('stdio');

var opts = stdio.getopt({
    'key': {key: 'k', args: 1, description: 'SHA1 key.'},
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

function digest(s, k) {
    var sha1 = crypto.createHash('sha1', k);
    return sha1.update(s).digest();
}

var salt = '6dd59598fe1520e52bc3e91c54dfeb9f'; // for pbkdf2
var key = crypto.pbkdf2Sync('8a289e301d5e7e78ff49788c1328acfa', salt, 0, 16);
var seed = new Buffer('823fc6c81045addc425a6fd3681dad51', 'hex');
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
    var temp = new Buffer(digest(date, key));
    var out = new Buffer(digest(xor(seed, temp), key));
    seed = new Buffer(digest(xor(out, temp), key));
    console.log(new BigNumber(out.toString('hex'), 16).toString());
}
