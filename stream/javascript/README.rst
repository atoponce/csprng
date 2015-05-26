Dependencies
============

* https://github.com/MikeMcl/bignumber.js/
* https://travis-ci.org/sgmonda/stdio 

Randomness Tests
================

RC4 in counter mode
-------------------

::

    $ ./rc4_counter.js -b -n 250000 | rngtest 
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
    rngtest: input channel speed: (min=287.995; avg=2418.126; max=2981.415)Kibits/s
    rngtest: FIPS tests speed: (min=89.547; avg=146.173; max=150.185)Mibits/s
    rngtest: Program run time: 13429646 microseconds

ANSI x9.17 DRBG
---------------

::

    $ ./ansi_x9.17.js -b -n 250000 | rngtest 
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
    rngtest: input channel speed: (min=283.033; avg=1488.677; max=1844.485)Kibits/s
    rngtest: FIPS tests speed: (min=100.918; avg=146.562; max=150.185)Mibits/s
    rngtest: Program run time: 21506884 microseconds
