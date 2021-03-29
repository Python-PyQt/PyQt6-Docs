.. sip:method-description::
    :status: todo
    :pysig: 128bb55d27fc765f89944a64fae19162
    :realsig: (qsizetype,qsizetype) const
    :digest: 42ee7ef29a906aac56d682a9a01f84cc

Returns a byte array containing the *n* bytes of this object starting at position *pos*.

**Note:** The behavior is undefined when *pos* < 0, *n* < 0, or *pos* + *n* > :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 294-296

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.last`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
