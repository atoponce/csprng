Dependencies
============

* https://www.dlitz.net/software/pycrypto/

Randomness Tests
================

SHA-1 in counter mode
---------------------

::

    $ ./sha1_counter.py -b -n 250000 | rngtest 
    rngtest 2-unofficial-mt.14
    Copyright (c) 2004 by Henrique de Moraes Holschuh
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    rngtest: starting FIPS tests...
    rngtest: entropy source exhausted!
    rngtest: bits received from input: 40000000
    rngtest: FIPS 140-2 successes: 1999
    rngtest: FIPS 140-2 failures: 0
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 0
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=6.807; avg=25.852; max=16.528)Mibits/s
    rngtest: FIPS tests speed: (min=68.364; avg=140.666; max=150.185)Mibits/s
    rngtest: Program run time: 1767182 microseconds

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
    rngtest: bits received from input: 40000000
    rngtest: FIPS 140-2 successes: 1999
    rngtest: FIPS 140-2 failures: 0
    rngtest: FIPS 140-2(2001-10-10) Monobit: 0
    rngtest: FIPS 140-2(2001-10-10) Poker: 0
    rngtest: FIPS 140-2(2001-10-10) Runs: 0
    rngtest: FIPS 140-2(2001-10-10) Long run: 0
    rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
    rngtest: input channel speed: (min=1.594; avg=5.542; max=19073.486)Mibits/s
    rngtest: FIPS tests speed: (min=88.714; avg=133.213; max=150.185)Mibits/s
    rngtest: Program run time: 7191024 microseconds
