#!/usr/bin/node

var BigNumber = require('bignumber');
var crypto = require('crypto');
var stdio = require('stdio');

var opts = stdio.getopt({
    'binary': {key: 'b', args: 0, description: 'Raw binary output.'},
    'key': {key: 'k', args: 1, description: 'SHA-1 key.'},
    'numbers': {key: 'n', args: 1, description: 'Quantity of random numbers.'}
});

function digest(s) {
    var sha1 = crypto.createHash('sha1');
    return sha1.update(s).digest();
}

var salt = 'ce7b67344bcf92a881ea392ed0904fa6'; // for pbkdf2
var key = crypto.pbkdf2Sync('59947d9ef5fc733f95ea300c1ec8fa11', salt, 0, 16);
var number = 1;

if(opts.key) key = crypto.pbkdf2Sync(opts.key, salt, 0, 16);
if(opts.numbers) number = opts.numbers;

// Almost never return exponential notation
BigNumber.config({ EXPONENTIAL_AT: 1e+9 });

var counter = Date.now();

for (var i=0; i<number; i++) {
    var out = new Buffer(digest(counter+key));
    counter++;
    if(opts.binary) process.stdout.write(out);
    else console.log(new BigNumber(out.toString('hex'), 16).toString());
}
