.. sip:method-description::
    :status: todo
    :pysig: 0bb8e0816b62d336c21e7d194e3f0990
    :realsig: (const QDomCharacterData&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
