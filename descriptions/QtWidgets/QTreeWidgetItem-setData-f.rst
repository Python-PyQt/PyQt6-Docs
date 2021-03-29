.. sip:method-description::
    :status: todo
    :pysig: 5ec85c0fa5cfa5c1fac7e0bb6bc1272f
    :realsig: (int,int,const QVariant&)
    :digest: 4ed93864cbfcff592b6c43648f7bd06f

Sets the value for the item's *column* and *role* to the given *value*.

The *role* describes the type of data specified by *value*, and is defined by the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole` enum.

**Note:** The default implementation treats :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` as referring to the same data.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.data`.
