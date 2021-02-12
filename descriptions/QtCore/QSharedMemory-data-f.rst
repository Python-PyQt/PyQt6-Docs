.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: ()
    :digest: 405e9daef80c22b7bf09b3fdf8536d69

Returns a pointer to the contents of the shared memory segment, if one is attached. Otherwise it returns null. Remember to lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing to the shared memory, and remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.
