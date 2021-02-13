.. sip:method-description::
    :status: todo
    :pysig: 7625cd190ea18df4ca16eccb8dff07ea
    :realsig: (const QVariant&,int)
    :digest: dbfed34ab7bafdba2ed5606ffcbb4713

Sets the item's data for the given *role* to the specified *value*.

If you subclass :sip:ref:`~PyQt6.QtGui.QStandardItem` and reimplement this function, your reimplementation should call :sip:ref:`~PyQt6.QtGui.QStandardItem.emitDataChanged` if you do not call the base implementation of . This will ensure that e.g. views using the model are notified of the changes.

**Note:** The default implementation treats :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` as referring to the same data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`, :sip:ref:`~PyQt6.QtGui.QStandardItem.data`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setFlags`.
