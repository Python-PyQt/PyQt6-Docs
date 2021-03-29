.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1215fc16eefb36da3e2ba33a8fdd6f45

Locks the lock for reading. This function will block the current thread if another thread has locked for writing.

It is not possible to lock for read if the thread already has locked for write.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.tryLockForRead`.
