Dependencies
============

* https://github.com/MikeMcl/bignumber.js/
* https://travis-ci.org/sgmonda/stdio 

Randomness Tests
================

AES in counter mode
-------------------

    $ ./aes_counter.js -b -n 250000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    
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
    rngtest: input channel speed: (min=301.167; avg=4652.379; max=6204.336)Kibits/s
    rngtest: FIPS tests speed: (min=86.698; avg=146.185; max=150.185)Mibits/s
    rngtest: Program run time: 7227793 microseconds

ANSI x9.17 DRBG
---------------

    $ ./ansi_x9.17.js -b -n 250000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 32000000
    rngtest: FIPS 140-2 successes: 1596
    rngtest: FIPS 140-2 failures: 3
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 1
    rngtest: FIPS 140-2(2001-10-10) Long run: 2
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=281.369; avg=1567.721; max=1932.257)Kibits/s
    rngtest: FIPS tests speed: (min=92.590; avg=146.608; max=150.185)Mibits/s
    rngtest: Program run time: 20448629 microseconds
