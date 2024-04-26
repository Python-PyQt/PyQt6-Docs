.. sip:method-description::
    :status: todo
    :pysig: 132ef9df1f4642ade15be878398fab29
    :realsig: (int) const
    :digest: 074c5c1e0e5b92b3b5e13b482cf515b8

Returns the item's data for the given *role*, or an invalid :sip:ref:`~PyQt6.QtCore.QVariant` if there is no data for the role.

If you reimplement this function, your reimplementation should call the base implementation for roles you don't handle, otherwise getting flags, e.g. by calling :sip:ref:`~PyQt6.QtGui.QStandardItem.flags`, :sip:ref:`~PyQt6.QtGui.QStandardItem.isCheckable`, :sip:ref:`~PyQt6.QtGui.QStandardItem.isEditable` etc., will not work.

**Note:** The default implementation treats :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` as referring to the same data.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.setData`.
