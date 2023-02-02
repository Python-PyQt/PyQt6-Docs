.. sip:method-description::
    :status: todo
    :pysig: 9d5f3afb9455bc798ab36f723ee8cbf1
    :realsig: (const QMetaMethod&) const
    :digest: 215fe37cae8fc590b3afb664d642e1cb

Returns ``true`` if the *signal* is connected to at least one receiver, otherwise returns ``false``.

*signal* must be a signal member of this object, otherwise the behaviour is undefined.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 489-494

As the code snippet above illustrates, you can use this function to avoid expensive initialization or emitting a signal that nobody listens to. However, in a multithreaded application, connections might change after this function returns and before the signal gets emitted.

**Warning:** This function violates the object-oriented principle of modularity. In particular, this function must not be called from an override of :sip:ref:`~PyQt6.QtCore.QObject.connectNotify` or :sip:ref:`~PyQt6.QtCore.QObject.disconnectNotify`, as those might get called from any thread.
