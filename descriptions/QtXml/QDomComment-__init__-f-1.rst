.. sip:method-description::
    :status: todo
    :pysig: 019711918bfe296b45d96a70ac91627a
    :realsig: (const QDomComment&)
    :digest: 7dbd658cde70a33cb21ba3aa654fa85a

Constructs a copy of *comment*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
