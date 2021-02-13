.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 78741488dde5d979e7f7ddae4a4d76f9

Deletes all the text in the text edit.

Notes:

* The undo/redo history is also cleared.

* :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.currentCharFormat` is reset, unless :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.textCursor` is already at the beginning of the document.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.cut`, :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setPlainText`.
