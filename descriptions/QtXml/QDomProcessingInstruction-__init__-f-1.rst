.. sip:method-description::
    :status: todo
    :pysig: 68d2b59f49956c495d0375847fbe281e
    :realsig: (const QDomProcessingInstruction&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
