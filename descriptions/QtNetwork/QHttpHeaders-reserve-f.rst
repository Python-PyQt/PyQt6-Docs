.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: a0c1b9ec2852675bd1a79c7771d4fb4f

Attempts to allocate memory for at least *size* header entries.

If you know in advance how how many header entries there will be, you may call this function to prevent reallocations and memory fragmentation.
