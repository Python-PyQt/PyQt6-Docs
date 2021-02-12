.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (qsizetype) const
    :digest: 57c1ccba94805192e25320a56221ff7c

Returns the last *n* bytes of the byte array.

**Note:** The behavior is undefined when *n* < 0 or *n* > :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 287-289

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`, :sip:ref:`~PyQt6.QtCore.QByteArray.endsWith`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
