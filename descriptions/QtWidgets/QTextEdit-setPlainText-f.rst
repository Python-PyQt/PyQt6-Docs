.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 58a78e995a8d7a530d90072eb69fbdb6

Changes the text of the text edit to the string *text*. Any previous text is removed.

Notes:

* *text* is interpreted as plain text.

* The undo/redo history is also cleared.

* :sip:ref:`~PyQt6.QtWidgets.QTextEdit.currentCharFormat` is reset, unless :sip:ref:`~PyQt6.QtWidgets.QTextEdit.textCursor` is already at the beginning of the document.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit.toPlainText`.
