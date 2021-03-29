.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 5395aba55cd843b1214b6e1747b3c1bf

Returns the size of the attached shared memory segment. If no shared memory segment is attached, 0 is returned.

**Note:** The size of the segment may be larger than the requested size that was passed to :sip:ref:`~PyQt6.QtCore.QSharedMemory.create`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.create`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.
