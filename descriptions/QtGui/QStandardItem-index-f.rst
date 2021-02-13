.. sip:method-description::
    :status: todo
    :pysig: af193f7da54d4df813f044d1a85c747b
    :realsig: () const
    :digest: 699be8047f36c2fbe54fa4c3da6d1047

Returns the :sip:ref:`~PyQt6.QtCore.QModelIndex` associated with this item.

When you need to invoke item functionality in a :sip:ref:`~PyQt6.QtCore.QModelIndex`-based API (e.g. :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`), you can call this function to obtain an index that corresponds to the item's location in the model.

If the item is not associated with a model, an invalid :sip:ref:`~PyQt6.QtCore.QModelIndex` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.model`, :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemFromIndex`.
