.. sip:method-description::
    :status: todo
    :pysig: 9d5f3afb9455bc798ab36f723ee8cbf1
    :realsig: (const QMetaMethod&) const
    :digest: 9589b02971fb80c3fc7b78178d538261

Returns ``true`` if the *signal* is connected to at least one receiver, otherwise returns ``false``.

*signal* must be a signal member of this object, otherwise the behaviour is undefined.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 489-494

As the code snippet above illustrates, you can use this function to avoid expensive operations or emitting a signal that nobody listens to.

**Warning:** In a multithreaded application, consecutive calls to this function are not guaranteed to yield the same results.

**Warning:** This function violates the object-oriented principle of modularity. In particular, this function must not be called from an override of :sip:ref:`~PyQt6.QtCore.QObject.connectNotify` or :sip:ref:`~PyQt6.QtCore.QObject.disconnectNotify`, as those might get called from any thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.receivers`.
