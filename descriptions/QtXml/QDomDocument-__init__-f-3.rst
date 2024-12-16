.. sip:method-description::
    :status: todo
    :pysig: b37246b452bdb463423de850fa2050b8
    :realsig: (const QDomDocument&)
    :digest: 6d2cf70c8da850e1158848513a50b0d2

Constructs a copy of *document*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
