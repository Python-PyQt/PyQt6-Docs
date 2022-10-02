.. sip:signal-description::
    :status: todo
    :pysig: 500e8e01a8d8eae26e24d1bb8d33c9ce
    :realsig: (const QModelIndex&,int,int,const QModelIndex&,int)
    :digest: d4fd3216fb68208d6b5a4b8bab5b86a0

This signal is emitted after columns have been moved within the model. The items between *sourceStart* and *sourceEnd* inclusive, under the given *sourceParent* item have been moved to *destinationParent* starting at the column *destinationColumn*.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginMoveRows`.
