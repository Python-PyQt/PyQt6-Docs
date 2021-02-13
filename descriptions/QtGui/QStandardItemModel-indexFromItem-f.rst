.. sip:method-description::
    :status: todo
    :pysig: 0150d60f4079df73520d2a886f24e3c5
    :realsig: (const QStandardItem*) const
    :digest: 9e7843c36d252440e6434fe38f6ca696

Returns the :sip:ref:`~PyQt6.QtCore.QModelIndex` associated with the given *item*.

Use this function when you want to perform an operation that requires the :sip:ref:`~PyQt6.QtCore.QModelIndex` of the item, such as :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.scrollTo`. :sip:ref:`~PyQt6.QtGui.QStandardItem.index` is provided as convenience; it is equivalent to calling this function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemFromIndex`, :sip:ref:`~PyQt6.QtGui.QStandardItem.index`.
