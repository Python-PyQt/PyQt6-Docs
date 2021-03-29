.. sip:method-description::
    :status: todo
    :pysig: c0b1f26748a8a22542f8256ed7a18944
    :realsig: (const QDomAttr&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
