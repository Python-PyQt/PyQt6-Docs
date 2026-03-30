.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: c45d29c60347f1138964577db261aecc

Changes the text of the text edit to the string *text*. Any previous text is removed.

*text* is interpreted as plain text.

Notes:

* The undo/redo history is also cleared.

* :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.currentCharFormat` is reset, unless :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.textCursor` is already at the beginning of the document.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.toPlainText`.
