.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 7c93784d8a5919b7cff00803ef531972

Attempts to lock for writing. If the lock was obtained, this function returns ``true``; otherwise, it returns ``false`` immediately.

The lock attempt will fail if another thread has locked for reading or writing.

If the lock was obtained, the lock must be unlocked with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` before another thread can successfully lock it.

It is not possible to lock for write if the thread already has locked for read.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite`.
