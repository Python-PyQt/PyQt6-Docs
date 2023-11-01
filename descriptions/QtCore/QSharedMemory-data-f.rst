.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: ()
    :digest: 08e8e50998013a78f1d72cb5029b1806

Returns a pointer to the contents of the shared memory segment, if one is attached. Otherwise it returns null. The value returned by this function will not change until a :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` happens, so it is safe to store this pointer.

If the memory operations are not atomic, you may lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing, but remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.
