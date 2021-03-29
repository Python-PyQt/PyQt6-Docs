.. sip:method-description::
    :status: todo
    :pysig: 019711918bfe296b45d96a70ac91627a
    :realsig: (const QDomComment&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
