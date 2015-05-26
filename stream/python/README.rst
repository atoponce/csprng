Dependencies
============

* https://www.dlitz.net/software/pycrypto/

Randomness Tests
================

RC4 in counter mode
-------------------

::

    $ ./rc4_counter.py -b -n 250000 | rngtest 
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
    rngtest: input channel speed: (min=28.943; avg=175.011; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=59.051; avg=131.186; max=150.185)Mibits/s
    rngtest: Program run time: 439569 microseconds


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
    rngtest: FIPS 140-2 successes: 1598
    rngtest: FIPS 140-2 failures: 1
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 1
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=2.134; avg=7.096; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=88.714; avg=133.418; max=150.185)Mibits/s
    rngtest: Program run time: 4554773 microseconds
