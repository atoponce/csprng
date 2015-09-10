#!/bin/sh

for I in $(seq 5000 5000 100000); do
    echo $I
    /usr/bin/time ../block/javascript/ansi_x9.17.js -n $I > /dev/null 2>> block_javascript.txt
    /usr/bin/time ../block/perl/ansi_x9.17.pl -n $I > /dev/null 2>> block_perl.txt
    /usr/bin/time ../block/python/ansi_x9.17.py -n $I > /dev/null 2>> block_python.txt
    /usr/bin/time ../hash/javascript/ansi_x9.17.js -n $I > /dev/null 2>> hash_javascript.txt
    /usr/bin/time ../hash/perl/ansi_x9.17.pl -n $I > /dev/null 2>> hash_perl.txt
    /usr/bin/time ../hash/python/ansi_x9.17.py -n $I > /dev/null 2>> hash_python.txt
    /usr/bin/time ../stream/javascript/ansi_x9.17.js -n $I > /dev/null 2>> stream_javascript.txt
    /usr/bin/time ../stream/perl/ansi_x9.17.pl -n $I > /dev/null 2>> stream_perl.txt
    /usr/bin/time ../stream/python/ansi_x9.17.py -n $I > /dev/null 2>> stream_python.txt
done
