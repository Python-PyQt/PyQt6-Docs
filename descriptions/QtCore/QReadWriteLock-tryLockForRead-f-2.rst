.. sip:method-description::
    :status: todo
    :pysig: 9c39f5b2bffde62b56ab06a7f61d6ae6
    :realsig: (QDeadlineTimer)
    :digest: 0d5ecbd33b6c58cdbbf39bd5ec1c28c0

This is an overloaded function.

Attempts to lock for reading. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked for writing, this function will wait until *timeout* expires for the lock to become available.

If the lock was obtained, the lock must be unlocked with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` before another thread can successfully lock it for writing.

It is not possible to lock for read if the thread already has locked for write.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead`.
