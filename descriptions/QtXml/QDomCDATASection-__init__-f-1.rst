.. sip:method-description::
    :status: todo
    :pysig: a5da4b3fd9e700bcc0b42de6009ddda0
    :realsig: (const QDomCDATASection&)
    :digest: 598a279d2b29f4d55af34022b7974ace

Constructs a copy of *cdataSection*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
