.. sip:method-description::
    :status: todo
    :pysig: 128bb55d27fc765f89944a64fae19162
    :realsig: (qsizetype, qsizetype)
    :digest: c1994f5f386da61c4c0445c536fc46e4

Modifies this byte array to start at position *pos*, extending for *n* bytes, and returns a reference to this byte array.

**Note:** The behavior is undefined if *pos* < 0, *n* < 0, or *pos* + *n* > :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`, :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.last`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
