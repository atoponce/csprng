Cryptographic PRNGs
===================

Why
---

This respository is a way for me to learn how to implement a CSPRNG in various
languages. No doubt, many languages come with access to a CSPRNG already, such
as ``window.crypt.getRandomValues()`` in JavaScript or ``os.urandom()`` in
Python. Regardless, learning how to implement your own CSPRNG correctly, can be
a good way to learn cryptographic primitives, some pitfalls of cryptography,
and overall, just learn the syntax and oddities of new languages.

How
---

This repository looks at three different ways to build a CSPRNG:

* Using block ciphers
* Using stream ciphers
* Using hash functions

Each algorithm will be implemented in various languages. First, I am familiar
with Python and JavaScript, so those will be implemented first. Other languages
to follow.

What
----

Each CSPRNG prints a random number in either decimal or raw binary form. The
range is dependent on the cryptographic primitive. Typically, it is [0, 2^128),
or [0, 2^160);

Cryptographic primitives currently used are:

* AES-128-EBC
* Rijndael-128-EBC
* SHA-1
* RC4

When
----

A possible use for each CSPRNG is for secure password generation. For example,
consider the following script that prints 80-bit entropy passwords::

    $ for P in $(find -name '*_counter.*' -o -name 'ansi_x9.17.*'); do
    > $P -b -k a1e46t2S70ZTurYaghs5/w -n 1000 | strings | \
    > grep -o '[a-hjkmnp-z2-9.]' | head -n 16 | tr -d '\n'; echo " (from $P)"
    > done
    3.87yf3tq3vqexrk (from ./stream/perl/ansi_x9.17.pl)
    2r7a6ctyf78z2h5z (from ./stream/perl/rc4_counter.pl)
    5778mkt2p.djgys5 (from ./stream/javascript/rc4_counter.js)
    a75fnfe58r3m3zby (from ./stream/javascript/ansi_x9.17.js)
    2kr65.m.5racgy8m (from ./stream/python/ansi_x9.17.py)
    whv.xxud5y.7.zd9 (from ./stream/python/rc4_counter.py)
    kfm868p947w95fsk (from ./hash/perl/ansi_x9.17.pl)
    6xhe36xt47p392g2 (from ./hash/perl/sha1_counter.pl)
    t537p8uu6pkv9hcr (from ./hash/javascript/sha1_counter.js)
    d8ujrmt6jbf3dyjk (from ./hash/javascript/ansi_x9.17.js)
    ncmnygcbt4qdpt23 (from ./hash/python/sha1_counter.py)
    x3wn7qcnw5evm2r2 (from ./hash/python/ansi_x9.17.py)
    m87q4ny749n2apc5 (from ./block/perl/ansi_x9.17.pl)
    8249cn5q.pbpahw4 (from ./block/perl/aes_counter.pl)
    k4rfb9djwu8hfbr8 (from ./block/javascript/aes_counter.js)
    c4r87.mnbf6932ax (from ./block/javascript/ansi_x9.17.js)
    ekxuuu6q6k7emaem (from ./block/python/ansi_x9.17.py)
    8yv4schdnshdgkut (from ./block/python/aes_counter.py)

License
-------

Unless otherwise stated, every implementation will not be licensed, but instead
released under the public domain.
