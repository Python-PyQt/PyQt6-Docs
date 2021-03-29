.. sip:method-description::
    :status: todo
    :pysig: 115a8fcb1bc1fc88cc09a9abe08d7988
    :realsig: (const QModelIndex&) const
    :digest: 0e02801ff43ad43bf475914c0e26c675

Returns the path for the given *index*. The completer object uses this to obtain the completion text from the underlying model.

The default implementation returns the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` of the item for list models. It returns the absolute file path if the model is a :sip:ref:`~PyQt6.QtGui.QFileSystemModel`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.splitPath`.
