.. sip:method-description::
    :status: todo
    :pysig: 6e60578a215cfb6c006cca2a9d60e308
    :realsig: (const QTextCharFormat&)
    :digest: 27f264eb299b756db507fd51760cfbd3

Merges the properties specified in *modifier* into the current character format by calling :sip:ref:`~PyQt6.QtGui.QTextCursor.mergeCharFormat` on the editor's cursor. If the editor has a selection then the properties of *modifier* are directly applied to the selection.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.mergeCharFormat`.
