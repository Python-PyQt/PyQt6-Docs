.. sip:method-description::
    :status: todo
    :pysig: f3efd09867f8e2da83d6b12e9b7ca068
    :realsig: (const char*) const
    :digest: e909958940ba569ec90af312a812bade

Returns the number of receivers connected to the *signal*.

Since both slots and signals can be used as receivers for signals, and the same connections can be made many times, the number of receivers is the same as the number of connections made from this signal.

When calling this function, you can use the ``SIGNAL()`` macro to pass a specific signal:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 273-277

**Warning:** This function violates the object-oriented principle of modularity. However, it might be useful when you need to perform expensive initialization only if something is connected to a signal.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.isSignalConnected`.
