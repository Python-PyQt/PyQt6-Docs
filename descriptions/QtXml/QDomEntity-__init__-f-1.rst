.. sip:method-description::
    :status: todo
    :pysig: ca4f07698e27c2c7ba0a5e3a51735ac0
    :realsig: (const QDomEntity&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
