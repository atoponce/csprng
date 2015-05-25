#!/usr/bin/node

var BigNumber = require('bignumber');
var crypto = require('crypto');
var stdio = require('stdio');

var opts = stdio.getopt({
    'key': {key: 'k', args: 1, description: 'AES key.'},
    'seed': {key: 's', args: 1, description: 'Starting seed.'},
    'numbers': {key: 'n', args: 1, description: 'Quantity of random numbers.'}
});

function sxor(s1, s2) {
    s1 = new Buffer(s1);
    s2 = new Buffer(s2);
    var xor = [];
    for (var i=0; i<s1.length; i++) {
        xor.push(s1[i]^s2[i]);
    }
    return new Buffer(xor);
}

function encrypt(str) {
    var aes = crypto.createCipher('aes128', key);
    return aes.update(str, 'utf8', 'hex') + aes.final('hex');
}

var salt = 'a149e11d6b49590b9b394568c603c9c1'; // for pbkdf2
var key = '63e007252ab90adf43fb0515bbb42c47';
var seed = new Buffer('0c2edeada47381a6590a56f37bcd1ac7', 'hex');
var number = 1;

if(opts.key) key = crypto.pbkdf2Sync(opts.key, salt, 0, 16).toString('hex');
if(opts.seed) seed = crypto.pbkdf2Sync(opts.seed, salt, 0, 16).toString('hex');
if(opts.numbers) number = opts.numbers;

for (var i=0; i<number; i++) {
    var date = (new Date).getTime().toString();
    var temp = new Buffer(encrypt(date), 'hex');
    var out = new Buffer(encrypt(sxor(seed, temp), 'hex'));

    console.log(out.toString());

    seed = new Buffer(encrypt(sxor(out, temp), 'hex'));
}
