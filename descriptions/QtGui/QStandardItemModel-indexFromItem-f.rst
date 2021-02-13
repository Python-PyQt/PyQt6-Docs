.. sip:method-description::
    :status: todo
    :pysig: 0150d60f4079df73520d2a886f24e3c5
    :realsig: (const QStandardItem*) const
    :digest: f487f823a724e44af2760d2d45f7a2ac

Returns the :sip:ref:`~PyQt6.QtCore.QModelIndex` associated with the given *item*.

Use this function when you want to perform an operation that requires the :sip:ref:`~PyQt6.QtCore.QModelIndex` of the item, such as QAbstractItemView::scrollTo(). :sip:ref:`~PyQt6.QtGui.QStandardItem.index` is provided as convenience; it is equivalent to calling this function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemFromIndex`, :sip:ref:`~PyQt6.QtGui.QStandardItem.index`.
