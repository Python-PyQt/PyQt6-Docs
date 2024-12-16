.. sip:method-description::
    :status: todo
    :pysig: e3cda5fab4eb6f1da568c6f72a94dfeb
    :realsig: (const QDomDocumentFragment&)
    :digest: 53a6ed755188de25cf4868fbfc83244c

Constructs a copy of *documentFragment*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
