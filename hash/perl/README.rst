Dependencies
============

* https://metacpan.org/pod/Digest::SHA
* https://metacpan.org/pod/Crypt::PBKDF2
* https://metacpan.org/pod/Getopt::Long
* https://metacpan.org/pod/Time::HiRes

Randomness Tests
================

SHA-1 in counter mode
---------------------

::

    $ ./sha1_counter.pl -b -n 250000 | rngtest
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 40000000
    rngtest: FIPS 140-2 successes: 1998
    rngtest: FIPS 140-2 failures: 1
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 1
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 0
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=76.294; avg=423.201; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=33.818; avg=128.975; max=150.185)Mibits/s
    rngtest: Program run time: 608930 microseconds

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
    rngtest: bits received from input: 40000000
    rngtest: FIPS 140-2 successes: 1998
    rngtest: FIPS 140-2 failures: 1
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 1
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=8.148; avg=34.774; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=55.446; avg=127.024; max=150.185)Mibits/s
    rngtest: Program run time: 1629903 microseconds
