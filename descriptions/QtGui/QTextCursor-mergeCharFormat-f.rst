.. sip:method-description::
    :status: todo
    :pysig: 6e60578a215cfb6c006cca2a9d60e308
    :realsig: (const QTextCharFormat&)
    :digest: e8f272b6e60e77df6865a43ac7c8a00b

Merges the cursor's current character format with the properties described by format *modifier*. If the cursor has a selection, this function applies all the properties set in *modifier* to all the character formats that are part of the selection.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.hasSelection`, :sip:ref:`~PyQt6.QtGui.QTextCursor.setCharFormat`.
