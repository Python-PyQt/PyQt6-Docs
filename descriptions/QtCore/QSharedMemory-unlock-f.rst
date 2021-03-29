.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 00dfff9f54eef9a99ab721666ef73ddd

Releases the lock on the shared memory segment and returns ``true``, if the lock is currently held by this process. If the segment is not locked, or if the lock is held by another process, nothing happens and false is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock`.
