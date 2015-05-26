#!/usr/bin/perl
use strict;

use Crypt::PBKDF2;      # requires libcrypt-pbkdf2-perl
use Crypt::RC4;
use Getopt::Long qw(GetOptions);
use Time::HiRes;

my $b;  # display raw binary output
my $k;  # user-supplied key
my $n;  # user-supplied rounds
my $h;  # display usage

my $number;
my $pbkdf2;

my $res = GetOptions(
    "b|binary"    => \$b,
    "k|key=s"     => \$k,
    "n|numbers=i" => \$n,
    "h|help"      => \$h,
);

my $salt = pack("H*", '49740e7049d8dbb5f6a032548d2d7c11');  # for Crypt::PBKDF2
my $key = pack("H*", '51d3a356bc03218f91e5db52b69cdc15');

$pbkdf2 = Crypt::PBKDF2->new(
    # 0 iterations guarantees high performance 16-byte output
    # the security rests on the entropy of $key, not iterating pkdf2
    hash_class  => 'HMACSHA1',
    iterations  => 0,
    output_len  => 16,
    salt_len    => 4,
);

if ($h) {
    print "usage: ansi_x9.17.prl [-h] [-k KEY] [-s SEED] [-n NUMBERS]

RC4 in counter mode CSPRNG

optional arguments:
  -h, --help            show this help message and exit
  -b, --binary          Raw binary output.
  -k KEY, --key KEY     AES key.
  -n NUMBERS, --numbers NUMBERS
                        Quantity of random numbers.
";
    exit;
}

$key = $pbkdf2->PBKDF2($k, $salt) if ($k);
$number = ($n ? int($n) : 1);

my $rc4 = Crypt::RC4->new($key);
my $counter = Time::HiRes::time()*1000000;

for (my $i=0; $i<$number; $i++) {
    my $out = $rc4->RC4(sprintf("%016d", $counter));
    $counter++;
    if ($b) { print $out; }
    else { print unpack("QQ", $out), "\n"; }
}
