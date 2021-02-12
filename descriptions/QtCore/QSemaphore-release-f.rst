.. sip:method-description::
    :status: todo
    :pysig: cd756c5b6e9231f18958d85978fd7238
    :realsig: (int)
    :digest: 2698eb99bb0adb7fb543f39fac691210

Releases *n* resources guarded by the semaphore.

This function can be used to "create" resources as well. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 67-70

:sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` is a `RAII <http://en.cppreference.com/w/cpp/language/raii>`_ wrapper around this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSemaphore.acquire`, :sip:ref:`~PyQt6.QtCore.QSemaphore.available`, :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser`.
