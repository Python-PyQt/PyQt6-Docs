.. sip:method-description::
    :status: todo
    :pysig: 4a42274a196ae8939c5e475058db8e8e
    :realsig: () const
    :digest: b206c619be90023aceca2939daf5cb73

Returns the current selection (which may be empty) with all its formatting information. If you just want the selected text (i.e. plain text) use :sip:ref:`~PyQt6.QtGui.QTextCursor.selectedText` instead.

**Note:** Unlike :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toPlainText`, :sip:ref:`~PyQt6.QtGui.QTextCursor.selectedText` may include special unicode characters such as QChar::ParagraphSeparator.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toPlainText`.
