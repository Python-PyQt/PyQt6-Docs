.. sip:method-description::
    :status: todo
    :pysig: f3efd09867f8e2da83d6b12e9b7ca068
    :realsig: (const char*) const
    :digest: 494fb56304cfae17bc5f67ec97de4916

Returns the number of receivers connected to the *signal*.

Since both slots and signals can be used as receivers for signals, and the same connections can be made many times, the number of receivers is the same as the number of connections made from this signal.

When calling this function, you can use the ``SIGNAL()`` macro to pass a specific signal:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 273-277

As the code snippet above illustrates, you can use this function to avoid expensive operations or emitting a signal that nobody listens to.

**Warning:** In a multithreaded application, consecutive calls to this function are not guaranteed to yield the same results.

**Warning:** This function violates the object-oriented principle of modularity. In particular, this function must not be called from an override of :sip:ref:`~PyQt6.QtCore.QObject.connectNotify` or :sip:ref:`~PyQt6.QtCore.QObject.disconnectNotify`, as those might get called from any thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.isSignalConnected`.
