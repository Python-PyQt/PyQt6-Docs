.. sip:method-description::
    :status: todo
    :pysig: 770e1785bf230215c95e86b61944a276
    :realsig: () const
    :digest: 0d7a1cf6252cb29666e5fdfdba08b340

This function returns a new MIME data object to represent the contents of the text edit's current selection. It is called when the selection needs to be encapsulated into a new :sip:ref:`~PyQt6.QtCore.QMimeData` object; for example, when a drag and drop operation is started, or when data is copied to the clipboard.

If you reimplement this function, note that the ownership of the returned :sip:ref:`~PyQt6.QtCore.QMimeData` object is passed to the caller. The selection can be retrieved by using the :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.textCursor` function.
