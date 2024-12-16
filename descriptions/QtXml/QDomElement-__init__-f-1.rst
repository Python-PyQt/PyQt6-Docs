.. sip:method-description::
    :status: todo
    :pysig: e74187423ce486f1db9b26f02489a275
    :realsig: (const QDomElement&)
    :digest: 6f92592bf192ed05dcf99171a67265b2

Constructs a copy of *element*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
