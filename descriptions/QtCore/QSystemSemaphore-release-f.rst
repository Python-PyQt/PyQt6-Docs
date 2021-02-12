.. sip:method-description::
    :status: todo
    :pysig: e9b4c34a27f45ab7af3785c6b51ad455
    :realsig: (int)
    :digest: fd918b7cd377b3ae68305d9bfc31e9cf

Releases *n* resources guarded by the semaphore. Returns ``true`` unless there is a system error.

Example: Create a system semaphore having five resources; acquire them all and then release them all.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qsystemsemaphore.py
    :lines: 65-68

This function can also "create" resources. For example, immediately following the sequence of statements above, suppose we add the statement:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qsystemsemaphore.py
    :lines: 73-73

Ten new resources are now guarded by the semaphore, in addition to the five that already existed. You would not normally use this function to create more resources.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire`.
