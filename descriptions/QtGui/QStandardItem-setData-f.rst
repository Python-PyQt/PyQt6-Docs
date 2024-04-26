.. sip:method-description::
    :status: todo
    :pysig: 7625cd190ea18df4ca16eccb8dff07ea
    :realsig: (const QVariant&,int)
    :digest: 74884eb18e8b2fc920399fe7bc88382a

Sets the item's data for the given *role* to the specified *value*.

If you subclass :sip:ref:`~PyQt6.QtGui.QStandardItem` and reimplement this function, your reimplementation should:

* call :sip:ref:`~PyQt6.QtGui.QStandardItem.emitDataChanged` if you do not call the base implementation of setData(). This will ensure that e.g. views using the model are notified of the changes

* call the base implementation for roles you don't handle, otherwise setting flags, e.g. by calling :sip:ref:`~PyQt6.QtGui.QStandardItem.setFlags`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setCheckable`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setEditable` etc., will not work.

**Note:** The default implementation treats :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` as referring to the same data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`, :sip:ref:`~PyQt6.QtGui.QStandardItem.data`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setFlags`.
