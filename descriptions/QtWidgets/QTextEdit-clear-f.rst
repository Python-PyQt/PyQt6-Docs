.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3ea141ac5936023ae9f4da0ba2655626

Deletes all the text in the text edit.

Notes:

* The undo/redo history is also cleared.

* :sip:ref:`~PyQt6.QtWidgets.QTextEdit.currentCharFormat` is reset, unless :sip:ref:`~PyQt6.QtWidgets.QTextEdit.textCursor` is already at the beginning of the document.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit.cut`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setPlainText`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setHtml`.
