.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: 3808aba375f182ccbf2d1cc62727d56a

Removes *n* bytes from the end of the byte array.

If *n* is greater than :sip:ref:`~PyQt6.QtCore.QByteArray.size`, the result is an empty byte array.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 152-153

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`, :sip:ref:`~PyQt6.QtCore.QByteArray.resize`, :sip:ref:`~PyQt6.QtCore.QByteArray.first`.
