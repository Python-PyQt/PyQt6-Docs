.. sip:method-description::
    :status: todo
    :pysig: c567edb399b702bd49a6f5ea4ea59c51
    :realsig: (const QMetaMethod&)
    :digest: 62cc492ac0b0a2b9a67e90c34685c367

This virtual function is called when something has been connected to *signal* in this object.

If you want to compare *signal* with a specific signal, you can use QMetaMethod::fromSignal() as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 357-359

**Warning:** This function violates the object-oriented principle of modularity. However, it might be useful when you need to perform expensive initialization only if something is connected to a signal.

**Warning:** This function is called from the thread which performs the connection, which may be a different thread from the thread in which this object lives.

.. seealso:: connect(), :sip:ref:`~PyQt6.QtCore.QObject.disconnectNotify`.
