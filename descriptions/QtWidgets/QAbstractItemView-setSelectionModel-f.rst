.. sip:method-description::
    :status: todo
    :pysig: 9d7acca20c3a0945a5e1e6e5f12ea4ba
    :realsig: (QItemSelectionModel*)
    :digest: 2dd4171d3fef11f4d832a79436a38891

Sets the current selection model to the given *selectionModel*.

Note that, if you call :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setModel` after this function, the given *selectionModel* will be replaced by one created by the view.

**Note:** It is up to the application to delete the old selection model if it is no longer needed; i.e., if it is not being used by other views. This will happen automatically when its parent object is deleted. However, if it does not have a parent, or if the parent is a long-lived object, it may be preferable to call its deleteLater() function to explicitly delete it.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionModel`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setModel`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.clearSelection`.
