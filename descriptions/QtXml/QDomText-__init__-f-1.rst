.. sip:method-description::
    :status: todo
    :pysig: ae98cd938cc533f4d20ff9599a931c2d
    :realsig: (const QDomText&)
    :digest: ea98d3979a8db552445470d697bd7cdd

Constructs a copy of *text*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
