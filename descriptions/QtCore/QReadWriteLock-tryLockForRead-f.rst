.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 1ff704eedd2beccd846c4b80504d10db

Attempts to lock for reading. If the lock was obtained, this function returns ``true``, otherwise it returns ``false`` instead of waiting for the lock to become available, i.e. it does not block.

The lock attempt will fail if another thread has locked for writing.

If the lock was obtained, the lock must be unlocked with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` before another thread can successfully lock it for writing.

It is not possible to lock for read if the thread already has locked for write.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead`.
