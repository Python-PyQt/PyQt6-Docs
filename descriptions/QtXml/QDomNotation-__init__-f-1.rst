.. sip:method-description::
    :status: todo
    :pysig: eb57052fcf3983476c9ceb7374f88ff3
    :realsig: (const QDomNotation&)
    :digest: c8b5469cddd7dcd5f2baf0b63babc498

Constructs a copy of *notation*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
