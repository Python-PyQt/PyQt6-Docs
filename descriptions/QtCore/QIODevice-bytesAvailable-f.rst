.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: a1808cc24b9ece414c18d4d17e62c5ea

Returns the number of bytes that are available for reading. This function is commonly used with sequential devices to determine the number of bytes to allocate in a buffer before reading.

Subclasses that reimplement this function must call the base implementation in order to include the size of the buffer of :sip:ref:`~PyQt6.QtCore.QIODevice`. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qiodevice.py
    :lines: 68-71

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.bytesToWrite`, :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead`, :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential`.
