.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b361ff6fa678d9ac514f93df5ec7c0b8

Locks the lock for writing. This function will block the current thread if another thread (including the current) has locked for reading or writing (unless the lock has been created using the :sip:ref:`~PyQt6.QtCore.QReadWriteLock.RecursionMode.Recursive` mode).

It is not possible to lock for write if the thread already has locked for read.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.tryLockForWrite`.
