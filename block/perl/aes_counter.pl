#!/usr/bin/perl
use strict;

use Crypt::PBKDF2;      # requires libcrypt-pbkdf2-perl
use Crypt::Rijndael;
use Getopt::Long qw(GetOptions);
use Time::HiRes;

my $k;  # user-supplied key
my $n;  # user-supplied rounds
my $h;  # display usage

my $number;
my $pbkdf2;

my $res = GetOptions(
    "k|key=s"     => \$k,
    "n|numbers=i" => \$n,
    "h|help"      => \$h,
);

my $salt = pack('H*', 'b9a2625702639d9af9a5feec0f5d8c6b');  # for Crypt::PBKDF2
my $key = pack('H*', 'fbb8c6f40714f894f65d7a53e81b951e');

$pbkdf2 = Crypt::PBKDF2->new(
    hash_class  => 'HMACSHA1',
    # 0 iterations guarantees high performance 16-byte output
    # the security rests on the entropy of $key, not iterating pbkdf2
    iterations  => 0,
    output_len  => 16,
    salt_len    => 4,
);

if ($h) {
    print "usage: aes_counter.pl [-h] [-k KEY] [-s SEED] [-n NUMBERS]

AES in counter mode CSPRNG

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     AES key.
  -n NUMBERS, --numbers NUMBERS
                        Quantity of random numbers.
";
    exit;
}

$key = $pbkdf2->PBKDF2($k, $salt) if ($k);
$number = ($n ? int($n) : 1);

my $rijndael = Crypt::Rijndael->new($key);
my $counter = Time::HiRes::time()*1000000;

for (my $i=0; $i<$number; $i++) {
    my $out = $rijndael->encrypt(sprintf("%016d", $counter));
    print unpack("QQ", $out), "\n";
    $counter++;
}
