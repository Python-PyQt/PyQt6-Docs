.. sip:method-description::
    :status: todo
    :pysig: b37246b452bdb463423de850fa2050b8
    :realsig: (const QDomDocument&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
