Cryptographic Pseudorandom Number Generators
============================================

Why
---

This respository is a way for me to learn how to implement a CSPRNG in various
languages. No doubt, many languages come with access to a CSPRNG already, such
as ``window.crypt.getRandomValues()`` in JavaScript or ``os.urandom()`` in
Python. Regardless, learning how to implement your own CSPRNG correctly, can be
a good way to learn cryptographic primitives, some pitfalls of cryptography,
and overall, just learn the syntax and oddities of new languages.

What
----

This repository looks at three different ways to build a CSPRNG:

* Using block ciphers
* Using stream ciphers
* Using hash functions

Each algorithm will be implemented in various languages. First, I am familiar
with Python and JavaScript, so those will be implemented first. Other languages
to follow.

License
-------

Unless otherwise stated, every implementation will not be licensed, but instead
released under the public domain.
