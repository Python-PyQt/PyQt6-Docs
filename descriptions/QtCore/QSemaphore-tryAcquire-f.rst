.. sip:method-description::
    :status: todo
    :pysig: e9b4c34a27f45ab7af3785c6b51ad455
    :realsig: (int)
    :digest: dc5874fd28aa834983d571af122f0977

Tries to acquire ``n`` resources guarded by the semaphore and returns ``true`` on success. If :sip:ref:`~PyQt6.QtCore.QSemaphore.available` < *n*, this call immediately returns ``false`` without acquiring any resources.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 75-77

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSemaphore.acquire`.
