#!/usr/bin/perl
use strict;

use Crypt::PBKDF2;      # requires libcrypt-pbkdf2-perl
use Digest::SHA;
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

my $salt = pack('H*', '6e447d92b87553a7f893499b184b9411');  # for Crypt::PBKDF2
my $key = pack('H*', 'd9b251c8db1f88b58641260843a68c57');

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

SHA-1 in counter mode CSPRNG

optional arguments:
  -h, --help            Show this help message and exit.
  -b, --binary          Raw binary output.
  -k KEY, --key KEY     SHA-1 key.
  -n NUMBERS, --numbers NUMBERS
                        Quantity of random numbers.
";
    exit;
}

$key = $pbkdf2->PBKDF2($k, $salt) if ($k);
$number = ($n ? int($n) : 1);

my $counter = Time::HiRes::time()*1000000;

for (my $i=0; $i<$number; $i++) {
    my $out = Digest::SHA::sha1($key . $counter);
    $counter++;
    if ($b) { print $out; }
    else { print unpack("QQ", $out), "\n"; }
}
