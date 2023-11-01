.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: f3ea4f838326b74f6167fc0be650e8f5

Attempts to lock for reading. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked for writing, this function will wait for at most *timeout* milliseconds for the lock to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead`, i.e. this function will wait forever until lock can be locked for reading when *timeout* is negative.

If the lock was obtained, the lock must be unlocked with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` before another thread can successfully lock it for writing.

It is not possible to lock for read if the thread already has locked for write.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead`.
