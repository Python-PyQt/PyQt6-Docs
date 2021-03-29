.. sip:method-description::
    :status: todo
    :pysig: 35be435d5eb927e68aeed4ae67cd8a52
    :realsig: (qint64)
    :digest: 7fef4d22fedffaa66a3d4ef4ab302648

This is an overloaded function.

Peeks at most *maxSize* bytes from the device, returning the data peeked as a :sip:ref:`~PyQt6.QtCore.QByteArray`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qiodevice.py
    :lines: 107-110

This function has no way of reporting errors; returning an empty :sip:ref:`~PyQt6.QtCore.QByteArray` can mean either that no data was currently available for peeking, or that an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.read`.
