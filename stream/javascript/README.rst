Dependencies
============

* https://github.com/MikeMcl/bignumber.js/
* https://travis-ci.org/sgmonda/stdio 

Randomness Tests
================

RC4 in counter mode
-------------------

::

    $ ./rc4_counter.js -b -n 25000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 3200000
    rngtest: FIPS 140-2 successes: 158
    rngtest: FIPS 140-2 failures: 1
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 1
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=920.027; avg=2474.248; max=2941.453)Kibits/s
    rngtest: FIPS tests speed: (min=100.918; avg=145.578; max=149.012)Mibits/s
    rngtest: Program run time: 1367433 microseconds

ANSI x9.17 DRBG
---------------

::

    $ ./ansi_x9.17.js -b -n 25000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 3200000
    rngtest: FIPS 140-2 successes: 159
    rngtest: FIPS 140-2 failures: 0
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 0
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=422.855; avg=1492.586; max=1803.773)Kibits/s
    rngtest: FIPS tests speed: (min=126.314; avg=146.542; max=150.185)Mibits/s
    rngtest: Program run time: 2200005 microseconds
