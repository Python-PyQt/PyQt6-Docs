.. sip:signal-description::
    :status: todo
    :pysig: 500e8e01a8d8eae26e24d1bb8d33c9ce
    :realsig: (const QModelIndex&,int,int,const QModelIndex&,int)
    :digest: 2fa284611ee6a32f456006261d15c088

This signal is emitted after rows have been moved within the model. The items between *sourceStart* and *sourceEnd* inclusive, under the given *sourceParent* item have been moved to *destinationParent* starting at the row *destinationRow*.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginMoveRows`.
