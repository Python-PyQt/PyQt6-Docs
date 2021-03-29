.. sip:class-description::
    :status: todo
    :brief: Read-write locking
    :digest: e379a172bbdd155ff383e760f2ec2eaa

The :sip:ref:`~PyQt6.QtCore.QReadWriteLock` class provides read-write locking.

A read-write lock is a synchronization tool for protecting resources that can be accessed for reading and writing. This type of lock is useful if you want to allow multiple threads to have simultaneous read-only access, but as soon as one thread wants to write to the resource, all other threads must be blocked until the writing is complete.

In many cases, :sip:ref:`~PyQt6.QtCore.QReadWriteLock` is a direct competitor to :sip:ref:`~PyQt6.QtCore.QMutex`. :sip:ref:`~PyQt6.QtCore.QReadWriteLock` is a good choice if there are many concurrent reads and writing occurs infrequently.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qreadwritelock.py
    :lines: 54-72

To ensure that writers aren't blocked forever by readers, readers attempting to obtain a lock will not succeed if there is a blocked writer waiting for access, even if the lock is currently only accessed by other readers. Also, if the lock is accessed by a writer and another writer comes in, that writer will have priority over any readers that might also be waiting.

Like :sip:ref:`~PyQt6.QtCore.QMutex`, a :sip:ref:`~PyQt6.QtCore.QReadWriteLock` can be recursively locked by the same thread when constructed with :sip:ref:`~PyQt6.QtCore.QReadWriteLock.RecursionMode.Recursive` as :sip:ref:`~PyQt6.QtCore.QReadWriteLock.RecursionMode`. In such cases, :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` must be called the same number of times :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite` or :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead` was called. Note that the lock type cannot be changed when trying to lock recursively, i.e. it is not possible to lock for reading in a thread that already has locked for writing (and vice versa).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadLocker`, :sip:ref:`~PyQt6.QtCore.QWriteLocker`, :sip:ref:`~PyQt6.QtCore.QMutex`, :sip:ref:`~PyQt6.QtCore.QSemaphore`.
