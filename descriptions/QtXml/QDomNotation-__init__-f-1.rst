.. sip:method-description::
    :status: todo
    :pysig: eb57052fcf3983476c9ceb7374f88ff3
    :realsig: (const QDomNotation&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
