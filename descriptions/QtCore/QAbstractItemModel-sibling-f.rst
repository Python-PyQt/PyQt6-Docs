.. sip:method-description::
    :status: todo
    :pysig: 7ac02ca640a291bce69af9d99c614309
    :realsig: (int,int,const QModelIndex&) const
    :digest: fb32beaef37d607146a984d9ce6d95d8

Returns the sibling at *row* and *column* for the item at *index*, or an invalid :sip:ref:`~PyQt6.QtCore.QModelIndex` if there is no sibling at that location.

sibling() is just a convenience function that finds the item's parent, and uses it to retrieve the index of the child item in the specified *row* and *column*.

This method can optionally be overridden for implementation-specific optimization.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.index`, :sip:ref:`~PyQt6.QtCore.QModelIndex.row`, :sip:ref:`~PyQt6.QtCore.QModelIndex.column`.
