.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9a68871559901f2f7d8f500e5c72976e

Pastes the text from the clipboard into the text edit at the current cursor position.

If there is no text in the clipboard nothing happens.

To change the behavior of this function, i.e. to modify what :sip:ref:`~PyQt6.QtWidgets.QTextEdit` can paste and how it is being pasted, reimplement the virtual :sip:ref:`~PyQt6.QtWidgets.QTextEdit.canInsertFromMimeData` and :sip:ref:`~PyQt6.QtWidgets.QTextEdit.insertFromMimeData` functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit.cut`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.copy`.
