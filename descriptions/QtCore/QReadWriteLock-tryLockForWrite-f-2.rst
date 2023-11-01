.. sip:method-description::
    :status: todo
    :pysig: 9c39f5b2bffde62b56ab06a7f61d6ae6
    :realsig: (QDeadlineTimer)
    :digest: ed6a224b514f283c227fada8ce0bea9c

This is an overloaded function.

Attempts to lock for writing. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked for reading or writing, this function will wait until *timeout* expires for the lock to become available.

If the lock was obtained, the lock must be unlocked with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` before another thread can successfully lock it.

It is not possible to lock for write if the thread already has locked for read.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite`.
