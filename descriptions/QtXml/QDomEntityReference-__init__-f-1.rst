.. sip:method-description::
    :status: todo
    :pysig: 4706bf301d7ec0aa70a4532d4bf7b869
    :realsig: (const QDomEntityReference&)
    :digest: ab7c2b783a01f6b916660077a0265a2b

Constructs a copy of *entityReference*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
