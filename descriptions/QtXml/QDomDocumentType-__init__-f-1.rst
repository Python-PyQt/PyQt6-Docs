.. sip:method-description::
    :status: todo
    :pysig: fccb2dfc6af93cc1fee087cef002cec1
    :realsig: (const QDomDocumentType&)
    :digest: 61022c17cc1de5fbfaecabb4ebfa4c6f

Constructs a copy of *n*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
