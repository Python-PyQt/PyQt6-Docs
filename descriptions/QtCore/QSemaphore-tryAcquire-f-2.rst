.. sip:method-description::
    :status: todo
    :pysig: 163a34f24eb458a769e0786b1a72d01b
    :realsig: (int, QDeadlineTimer)
    :digest: 649076b55aa6622f01acc6657ac02b1a

Tries to acquire ``n`` resources guarded by the semaphore and returns ``true`` on success. If :sip:ref:`~PyQt6.QtCore.QSemaphore.available` < *n*, this call will wait until *timer* expires for resources to become available.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSemaphore.acquire`.
