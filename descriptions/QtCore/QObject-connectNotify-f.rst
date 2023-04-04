.. sip:method-description::
    :status: todo
    :pysig: c567edb399b702bd49a6f5ea4ea59c51
    :realsig: (const QMetaMethod&)
    :digest: 3854f838af17362577a4721c76352f1b

This virtual function is called when something has been connected to *signal* in this object.

If you want to compare *signal* with a specific signal, you can use QMetaMethod::fromSignal() as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 357-359

**Warning:** This function violates the object-oriented principle of modularity. However, it might be useful when you need to perform expensive initialization only if something is connected to a signal.

**Warning:** This function is called from the thread which performs the connection, which may be a different thread from the thread in which this object lives. This function may also be called with a :sip:ref:`~PyQt6.QtCore.QObject` internal mutex locked. It is therefore not allowed to re-enter any :sip:ref:`~PyQt6.QtCore.QObject` functions, including :sip:ref:`~PyQt6.QtCore.QObject.isSignalConnected`, from your reimplementation. If you lock a mutex in your reimplementation, make sure that you don't call :sip:ref:`~PyQt6.QtCore.QObject` functions with that mutex held in other places or it will result in a deadlock.

.. seealso:: connect(), :sip:ref:`~PyQt6.QtCore.QObject.disconnectNotify`.
