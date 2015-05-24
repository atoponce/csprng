#!/usr/bin/perl
use strict;

use Crypt::PBKDF2;      # requires libcrypt-pbkdf2-perl
use Digest::SHA;
use Getopt::Long qw(GetOptions);
use Time::HiRes;

my $k;  # user-supplied key
my $s;  # user-supplied seed
my $n;  # user-supplied rounds
my $h;  # display usage
my $number;
my $pbkdf2;

my $res = GetOptions(
    "k|key=s"     => \$k,
    "s|seed=s"    => \$s,
    "n|numbers=i" => \$n,
    "h|help"      => \$h,
);

my $salt = pack("H*", 'd28808258b51d61523209f72fcdc98ad');  # for Crypt::PBKDF2
my $key = pack("H*", 'bc87425f8aca7e6d5904e519a1f0122b');
my $seed = pack("H*", '9777fb02e408913fd51f20891b999093');

$pbkdf2 = Crypt::PBKDF2->new(
    hash_class  => 'HMACSHA1',
    # 0 iterations guarantees high performance 16-byte output
    # the security rests on the entropy of 'key', not iterating pbkdf2
    iterations  => 0,
    output_len  => 20,
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

$key = $pbkdf2->PBKDF2($k, $salt) if ($k);
$seed = $pbkdf2->PBKDF2($s, $salt) if ($s);
$number = ($n ? int($n) : 1);

# the actual ANSI X9.17 algorithm
for (my $i=0; $i<$number; $i++) {
    my $temp = Digest::SHA::sha1($key . Time::HiRes::time());
    my $out = Digest::SHA::sha1($seed ^ $temp);
    $seed = Digest::SHA::sha1($out ^ $temp);
    print unpack("QQ", $out), "\n";
}
