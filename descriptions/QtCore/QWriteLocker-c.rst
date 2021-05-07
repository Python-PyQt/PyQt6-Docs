.. sip:class-description::
    :status: todo
    :brief: Convenience class that simplifies locking and unlocking read-write locks for write access
    :digest: 23fd8fe6b99d1aeca7fa6500ce61c1bf

The :sip:ref:`~PyQt6.QtCore.QWriteLocker` class is a convenience class that simplifies locking and unlocking read-write locks for write access.

The purpose of :sip:ref:`~PyQt6.QtCore.QWriteLocker` (and :sip:ref:`~PyQt6.QtCore.QReadLocker`) is to simplify :sip:ref:`~PyQt6.QtCore.QReadWriteLock` locking and unlocking. Locking and unlocking statements or in exception handling code is error-prone and difficult to debug. :sip:ref:`~PyQt6.QtCore.QWriteLocker` can be used in such situations to ensure that the state of the lock is always well-defined.

Here's an example that uses :sip:ref:`~PyQt6.QtCore.QWriteLocker` to lock and unlock a read-write lock for writing:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qreadwritelock.py
    :lines: 102-108

It is equivalent to the following code:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qreadwritelock.py
    :lines: 113-120

The QMutexLocker documentation shows examples where the use of a locker object greatly simplifies programming.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadLocker`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock`.
