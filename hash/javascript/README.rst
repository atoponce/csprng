Dependencies
============

* https://github.com/MikeMcl/bignumber.js/
* https://travis-ci.org/sgmonda/stdio 

Randomness Tests
================

SHA-1 in counter mode
---------------------

``$ ./sha1_counter.js -b -n 250000 | rngtest 
rngtest 2-unofficial-mt.14
Copyright (c) 2004 by Henrique de Moraes Holschuh
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

rngtest: starting FIPS tests...
rngtest: entropy source exhausted!
rngtest: bits received from input: 40000000
rngtest: FIPS 140-2 successes: 1996
rngtest: FIPS 140-2 failures: 3
rngtest: FIPS 140-2(2001-10-10) Monobit: 0
rngtest: FIPS 140-2(2001-10-10) Poker: 0
rngtest: FIPS 140-2(2001-10-10) Runs: 2
rngtest: FIPS 140-2(2001-10-10) Long run: 1
rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
rngtest: input channel speed: (min=417.424; avg=5896.686; max=7704.635)Kibits/s
rngtest: FIPS tests speed: (min=112.861; avg=146.889; max=150.185)Mibits/s
rngtest: Program run time: 7144780 microseconds``

ANSI x9.17 DRBG
---------------

``$ ./ansi_x9.17.js -b -n 250000 | rngtest 
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
rngtest: input channel speed: (min=331.550; avg=2180.981; max=4184.072)Kibits/s
rngtest: FIPS tests speed: (min=71.436; avg=142.549; max=150.185)Mibits/s
rngtest: Program run time: 18426752 microseconds``
