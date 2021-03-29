.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 8ac5071f5959d344c0d90140c7874649

Returns ``true`` if a complete line of data can be read from the device; otherwise returns ``false``.

Note that unbuffered devices, which have no way of determining what can be read, always return false.

This function is often called in conjunction with the :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` signal.

Subclasses that reimplement this function must call the base implementation in order to include the contents of the :sip:ref:`~PyQt6.QtCore.QIODevice`'s buffer. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qiodevice.py
    :lines: 88-91

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead`, :sip:ref:`~PyQt6.QtCore.QIODevice.readLine`.
