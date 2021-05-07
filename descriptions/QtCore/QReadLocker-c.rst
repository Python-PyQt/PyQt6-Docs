.. sip:class-description::
    :status: todo
    :brief: Convenience class that simplifies locking and unlocking read-write locks for read access
    :digest: a3af41806dad016c63f2f665e2a04a61

The :sip:ref:`~PyQt6.QtCore.QReadLocker` class is a convenience class that simplifies locking and unlocking read-write locks for read access.

The purpose of :sip:ref:`~PyQt6.QtCore.QReadLocker` (and :sip:ref:`~PyQt6.QtCore.QWriteLocker`) is to simplify :sip:ref:`~PyQt6.QtCore.QReadWriteLock` locking and unlocking. Locking and unlocking statements or in exception handling code is error-prone and difficult to debug. :sip:ref:`~PyQt6.QtCore.QReadLocker` can be used in such situations to ensure that the state of the lock is always well-defined.

Here's an example that uses :sip:ref:`~PyQt6.QtCore.QReadLocker` to lock and unlock a read-write lock for reading:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qreadwritelock.py
    :lines: 77-84

It is equivalent to the following code:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qreadwritelock.py
    :lines: 89-97

The QMutexLocker documentation shows examples where the use of a locker object greatly simplifies programming.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QWriteLocker`, :sip:ref:`~PyQt6.QtCore.QReadWriteLock`.
