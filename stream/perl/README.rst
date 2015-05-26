Dependencies
============

* https://metacpan.org/pod/Crypt::RC4
* https://metacpan.org/pod/Crypt::PBKDF2
* https://metacpan.org/pod/Getopt::Long
* https://metacpan.org/pod/Time::HiRes

Randomness Tests
================

RC4 in counter mode
-------------------

``$ ./rc4_counter.pl -b -n 250000 | rngtest 
rngtest 2-unofficial-mt.14
Copyright (c) 2004 by Henrique de Moraes Holschuh
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

rngtest: starting FIPS tests...
rngtest: entropy source exhausted!
rngtest: bits received from input: 32000000
rngtest: FIPS 140-2 successes: 1599
rngtest: FIPS 140-2 failures: 0
rngtest: FIPS 140-2(2001-10-10) Monobit: 0
rngtest: FIPS 140-2(2001-10-10) Poker: 0
rngtest: FIPS 140-2(2001-10-10) Runs: 0
rngtest: FIPS 140-2(2001-10-10) Long run: 0
rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
rngtest: input channel speed: (min=996.340; avg=4414.318;
max=19531250.000)Kibits/s
rngtest: FIPS tests speed: (min=107.760; avg=147.022; max=150.185)Mibits/s
rngtest: Program run time: 7534134 microseconds``

ANSI x9.17 DRBG
---------------

``$ ./ansi_x9.17.pl -b -n 250000 | rngtest 
rngtest 2-unofficial-mt.14
Copyright (c) 2004 by Henrique de Moraes Holschuh
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

rngtest: starting FIPS tests...
rngtest: entropy source exhausted!
rngtest: bits received from input: 32000000
rngtest: FIPS 140-2 successes: 1598
rngtest: FIPS 140-2 failures: 1
rngtest: FIPS 140-2(2001-10-10) Monobit: 0
rngtest: FIPS 140-2(2001-10-10) Poker: 0
rngtest: FIPS 140-2(2001-10-10) Runs: 0
rngtest: FIPS 140-2(2001-10-10) Long run: 1
rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
rngtest: input channel speed: (min=210482.004; avg=1247765.298;
max=0.000)bits/s
rngtest: FIPS tests speed: (min=23.872; avg=126.949; max=150.185)Mibits/s
rngtest: Program run time: 26168854 microseconds``
