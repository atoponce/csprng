#!/usr/bin/perl
use strict;
use Getopt::Long qw(GetOptions);
use Crypt::Rijndael;
use Crypt::PBKDF2;      # requires libcrypt-pbkdf2-perl

my $k;  # user-supplied key
my $s;  # user-supplied seed
my $n;  # user-supplied rounds
my $h;  # display usage

my $key;
my $seed;
my $number;
my $date;
my $temp;
my $out;

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
    for (my $i=0; $i<32; $i++) {
        my $res = @s1[$i] ^ @s2[$i];
        $str .= chr($res);
    }
    return $str;
}

my $salt = 'f7c82a42cce025235dcebcabf75ebffb';  # for Crypt::PBKDF2
my $pbkdf2 = Crypt::PBKDF2->new(
    hash_class  => 'HMACSHA1',
    iterations  => 1000,
    output_len  => 16,
    salt_len    => 4,
);

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
    $key = $pbkdf2->PBKDF2_hex($k, $salt);
    $key = (split /:/, $key)[-1];
}
else {
    $key = $pbkdf2->PBKDF2_hex('044b8130e902fe475f5e9831f72da023', $salt);
    $key = (split /:/, $key)[-1];
}

if ($s) {
    $seed = $pbkdf2->PBKDF2_hex($s, $salt);
    $seed = (split /:/, $seed)[-1];
}
else {
    $seed = $pbkdf2->PBKDF2_hex('12155bf67b90e1deac3432a7db97e2b4', $salt);
    $seed = (split /:/, $seed)[-1];
}

if ($n) {
    $number = int($n);
}
else {
    $number = 1;
}

my $aes = Crypt::Rijndael->new($key);

# the actual ANSI X9.17 algorithm
for (my $i=0; $i<$number; $i++) {
    $date = $pbkdf2->PBKDF2_hex(time, $salt);
    $temp = $aes->encrypt($date);
    $out = $aes->encrypt(sxor($seed, $temp));
    $seed = $aes->encrypt(sxor($out, $temp));
    print int(unpack("Q*", $out))/2**64, "\n";
}