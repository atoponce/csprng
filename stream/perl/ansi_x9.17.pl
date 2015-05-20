#!/usr/bin/perl
use strict;

use bignum;
use Crypt::PBKDF2;      # requires libcrypt-pbkdf2-perl
use Crypt::RC4;
use Getopt::Long qw(GetOptions);
use Time::HiRes;

my $k;  # user-supplied key
my $s;  # user-supplied seed
my $n;  # user-supplied rounds
my $h;  # display usage

my $key;
my $seed;
my $number;
my $pbkdf2;

my $res = GetOptions(
    "k|key=s"     => \$k,
    "s|seed=s"    => \$s,
    "n|numbers=i" => \$n,
    "h|help"      => \$h,
);

sub sxor {
    my $str;
    my ($s1, $s2) = @_;
    my @s1 = unpack("C*", $s1);
    my @s2 = unpack("C*", $s2);
    for (my $i=0; $i<16; $i++) {
        my $res = @s1[$i] ^ @s2[$i];
        $str .= chr($res);
    }
    return $str;
}

my $salt = '2266ca556e5d565b04454d0bfda644e0';  # for Crypt::PBKDF2

{
    no bignum;
    $pbkdf2 = Crypt::PBKDF2->new(
        hash_class  => 'HMACSHA1',
        iterations  => 1000,
        output_len  => 16,
        salt_len    => 4,
    );
}

if ($h) {
    print "usage: ansi_x9.17.prl [-h] [-k KEY] [-s SEED] [-n NUMBERS]

ANSI x9.17 DRBG

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     AES key.
  -s SEED, --seed SEED  Starting seed.
  -n NUMBERS, --numbers NUMBERS
                        Quantity of random numbers.
";
    exit;
}

if ($k) {
    $key = $pbkdf2->PBKDF2($k, $salt);
    $key = (split /:/, $key)[-1];
}
else {
    $key = $pbkdf2->PBKDF2('a4160a248025e37ceb2112e889fef21d', $salt);
    $key = (split /:/, $key)[-1];
}

if ($s) {
    $seed = $pbkdf2->PBKDF2($s, $salt);
    $seed = (split /:/, $seed)[-1];
}
else {
    $seed = $pbkdf2->PBKDF2('8c98579689ce48eb90e9f20307d3f9b2', $salt);
    $seed = (split /:/, $seed)[-1];
}

if ($n) {
    $number = int($n);
}
else {
    $number = 1;
}

my $rc4 = Crypt::RC4->new($key);

# the actual ANSI X9.17 algorithm
for (my $i=0; $i<$number; $i++) {
    my $date = $pbkdf2->PBKDF2(Time::HiRes::time(), $salt);
    my $temp = $rc4->RC4($date);
    my $out = $rc4->RC4(sxor($seed, $temp));
    $seed = $rc4->RC4(sxor($out, $temp));
    print hex(unpack("H*", $out)), "\n";
}