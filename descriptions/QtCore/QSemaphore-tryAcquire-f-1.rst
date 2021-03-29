.. sip:method-description::
    :status: todo
    :pysig: d7eb8f2a66339e995244a3835a72b4b1
    :realsig: (int,int)
    :digest: ddc583cb45f8f7f10816e5df769114e4

Tries to acquire ``n`` resources guarded by the semaphore and returns ``true`` on success. If :sip:ref:`~PyQt6.QtCore.QSemaphore.available` < *n*, this call will wait for at most *timeout* milliseconds for resources to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QSemaphore.acquire`, i.e. this function will wait forever for resources to become available if *timeout* is negative.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 82-84

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSemaphore.acquire`.
