.. sip:method-description::
    :status: todo
    :pysig: e3cda5fab4eb6f1da568c6f72a94dfeb
    :realsig: (const QDomDocumentFragment&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
