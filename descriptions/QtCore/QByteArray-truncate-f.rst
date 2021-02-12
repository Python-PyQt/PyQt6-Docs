.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: c8883bf80fa70c5a6b1820a69681808d

Truncates the byte array at index position *pos*.

If *pos* is beyond the end of the array, nothing happens.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 146-147

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.resize`, :sip:ref:`~PyQt6.QtCore.QByteArray.first`.
