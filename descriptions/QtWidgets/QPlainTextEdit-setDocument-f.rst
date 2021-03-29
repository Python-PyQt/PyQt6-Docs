.. sip:method-description::
    :status: todo
    :pysig: f92e022cfaf3d7bdab73d5049018332a
    :realsig: (QTextDocument*)
    :digest: 14c15ba5d25cc0ced6e8db9f78806f5b

Makes *document* the new document of the text editor.

The parent :sip:ref:`~PyQt6.QtCore.QObject` of the provided document remains the owner of the object. If the current document is a child of the text editor, then it is deleted.

The document must have a document layout that inherits :sip:ref:`~PyQt6.QtWidgets.QPlainTextDocumentLayout` (see :sip:ref:`~PyQt6.QtGui.QTextDocument.setDocumentLayout`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.document`.
