Dependencies
============

* https://metacpan.org/pod/Crypt::Rijndael
* https://metacpan.org/pod/Crypt::PBKDF2
* https://metacpan.org/pod/Getopt::Long
* https://metacpan.org/pod/Time::HiRes

Randomness Tests
================

AES in counter mode
-------------------

::
    $ ./aes_counter.pl -b -n 250000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 32000000
    rngtest: FIPS 140-2 successes: 1595
    rngtest: FIPS 140-2 failures: 4
    rngtest: FIPS 140-2(2001-10-10) Monobit: 1
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 1
    rngtest: FIPS 140-2(2001-10-10) Long run: 2
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=43103448.276; avg=258800679.777; max=0.000)bits/s
    rngtest: FIPS tests speed: (min=119.209; avg=147.826; max=150.185)Mibits/s
    rngtest: Program run time: 563325 microseconds

ANSI x9.17 DRBG
---------------

::

    $ ./ansi_x9.17.pl -b -n 250000 | rngtest 
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
    rngtest: FIPS 140-2(2001-10-10) Runs: 1
    rngtest: FIPS 140-2(2001-10-10) Long run: 0
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=2571685.740; avg=9276478.210;
    max=0.000)bits/s
    rngtest: FIPS tests speed: (min=110.251; avg=147.064; max=150.185)Mibits/s
    rngtest: Program run time: 3898299 microseconds
