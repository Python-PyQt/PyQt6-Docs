.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: d936fc2c77a89b99daac11f8db14a1fa

Detaches the process from the shared memory segment. If this was the last process attached to the shared memory segment, then the shared memory segment is released by the system, i.e., the contents are destroyed. The function returns ``true`` if it detaches the shared memory segment. If it returns ``false``, it usually means the segment either isn't attached, or it is locked by another process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`.
