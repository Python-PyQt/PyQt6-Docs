.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 158f1b389a3323ddc4c9e57b96d54111

Returns a const pointer to the contents of the shared memory segment, if one is attached. Otherwise it returns null. The value returned by this function will not change until a :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` happens, so it is safe to store this pointer.

If the memory operations are not atomic, you may lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing, but remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.create`.
