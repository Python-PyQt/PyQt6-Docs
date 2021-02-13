.. sip:method-description::
    :status: todo
    :pysig: 4706bf301d7ec0aa70a4532d4bf7b869
    :realsig: (const QDomEntityReference&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
