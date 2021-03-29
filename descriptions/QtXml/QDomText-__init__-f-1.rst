.. sip:method-description::
    :status: todo
    :pysig: ae98cd938cc533f4d20ff9599a931c2d
    :realsig: (const QDomText&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
