.. sip:method-description::
    :status: todo
    :pysig: f3062fad2c6ede9f6dbf5902f073b767
    :realsig: ()
    :digest: 336be2d32a2f4c1f1810a535ee13f6bd

Cancels this :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` such that the destructor will no longer call ``semaphore()->release()``. Returns the value of :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser.semaphore` before this call. After this call, :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser.semaphore` will return ``nullptr``.

To enable again, assign a new :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 111-113
