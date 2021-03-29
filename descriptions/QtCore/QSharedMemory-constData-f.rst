.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 1944f3c61cc3b3f1bce5580b89d9a82f

Returns a const pointer to the contents of the shared memory segment, if one is attached. Otherwise it returns null. Remember to lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing to the shared memory, and remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.create`.
