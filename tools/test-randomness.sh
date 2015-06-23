#!/bin/bash

cd ~/src/csprng # change as necessary

for I in $(find -name '*.??' -executable -type f); do
    echo $I
    FILE=$(basename $I)
    F=${FILE%.*}
    D=$(dirname $I)/tests
    mkdir -p $D
    $I -b -n 46883 > $D/${F}.ent
    cp $D/${F}.ent $D/${F}.bmp
    dd if=./tools/blank.bmp of=$D/${F}.bmp bs=1 count=54 conv=notrunc 2> /dev/null
    ent $D/${F}.ent &> $D/${F}.txt
    rngtest < $D/${F}.ent &>> $D/${F}.txt
    dieharder -a < $D/${F}.ent &>> $D/${F}.txt
done
