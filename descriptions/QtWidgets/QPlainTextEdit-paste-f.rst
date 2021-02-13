.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9530775d55ba89d0d84bc54f2324bfb4

Pastes the text from the clipboard into the text edit at the current cursor position.

If there is no text in the clipboard nothing happens.

To change the behavior of this function, i.e. to modify what :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` can paste and how it is being pasted, reimplement the virtual :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.canInsertFromMimeData` and :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.insertFromMimeData` functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.cut`, :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.copy`.
