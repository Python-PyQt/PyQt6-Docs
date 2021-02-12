.. sip:method-description::
    :status: todo
    :pysig: e36193caa37d9025d5dfce060d04b01b
    :realsig: (const QModelIndex&,const QVariant&,int)
    :digest: 3c936932b6354924c47db87b3d4410a9

Sets the *role* data for the item at *index* to *value*.

Returns ``true`` if successful; otherwise returns ``false``.

The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged` signal should be emitted if the data was successfully set.

The base class implementation returns ``false``. This function and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` must be reimplemented for editable models.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.itemData`.
