.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (qsizetype) const
    :digest: 44cc5c821215fd9399272f43185f641b

Returns the first *n* bytes of the byte array.

**Note:** The behavior is undefined when *n* < 0 or *n* > :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 280-282

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.last`, :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`, :sip:ref:`~PyQt6.QtCore.QByteArray.startsWith`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
