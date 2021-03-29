.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b67a8d20f603b9295871943e3af6f7bc

Returns the number of bytes in this byte array.

The last byte in the byte array is at position  - 1. In addition, :sip:ref:`~PyQt6.QtCore.QByteArray` ensures that the byte at position  is always '\\0', so that you can use the return value of :sip:ref:`~PyQt6.QtCore.QByteArray.data` and constData() as arguments to functions that expect '\\0'-terminated strings. If the :sip:ref:`~PyQt6.QtCore.QByteArray` object was created from a raw data that didn't include the trailing '\\0'-termination byte, then :sip:ref:`~PyQt6.QtCore.QByteArray` doesn't add it automaticall unless a `deep copy <https://doc.qt.io/qt-6/implicit-sharing.html#deep-copy>`_ is created.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 112-116

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.isEmpty`, :sip:ref:`~PyQt6.QtCore.QByteArray.resize`.
