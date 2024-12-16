.. sip:method-description::
    :status: todo
    :pysig: fccb2dfc6af93cc1fee087cef002cec1
    :realsig: (const QDomDocumentType&)
    :digest: a2c17c3f79a53df9b3a21879a271ab6e

Constructs a copy of *documentType*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
