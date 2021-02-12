.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: 835b2a9a07e3c818d0439190cf9b7ad9

This is an overloaded function.

Attempts to lock for writing. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked for reading or writing, this function will wait for at most *timeout* milliseconds for the lock to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite`, i.e. this function will wait forever until lock can be locked for writing when *timeout* is negative.

If the lock was obtained, the lock must be unlocked with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` before another thread can successfully lock it.

It is not possible to lock for write if the thread already has locked for read.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite`.
