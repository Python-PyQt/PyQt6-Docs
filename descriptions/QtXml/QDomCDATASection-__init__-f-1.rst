.. sip:method-description::
    :status: todo
    :pysig: a5da4b3fd9e700bcc0b42de6009ddda0
    :realsig: (const QDomCDATASection&)
    :digest: 463a6ccdea6058ee546a89411bf9f667

Constructs a copy of *x*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
