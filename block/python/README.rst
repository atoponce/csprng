Dependencies
============

* https://www.dlitz.net/software/pycrypto/

Randomness Tests
================

AES in counter mode
-------------------

::

    $ ./aes_counter.py -b -n 250000 | rngtest 
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
    rngtest: input channel speed: (min=34.243; avg=171.092; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=86.698; avg=123.898; max=150.185)Mibits/s
    rngtest: Program run time: 446405 microseconds

ANSI x9.17 DRBG
---------------

::

    $ ./ansi_x9.17.py -b -n 250000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 32000000
    rngtest: FIPS 140-2 successes: 1597
    rngtest: FIPS 140-2 failures: 2
    rngtest: FIPS 140-2(2001-10-10) Monobit: 1
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 1
    rngtest: FIPS 140-2(2001-10-10) Long run: 0
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=3.333; avg=6.623; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=70.905; avg=145.546; max=150.185)Mibits/s
    rngtest: Program run time: 4844442 microseconds
