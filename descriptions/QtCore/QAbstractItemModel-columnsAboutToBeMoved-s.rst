.. sip:signal-description::
    :status: todo
    :pysig: 500e8e01a8d8eae26e24d1bb8d33c9ce
    :realsig: (const QModelIndex&,int,int,const QModelIndex&,int)
    :digest: b22b87d73fd41f6ba70613a752d0c50a

This signal is emitted just before columns are moved within the model. The items that will be moved are those between *sourceStart* and *sourceEnd* inclusive, under the given *sourceParent* item. They will be moved to *destinationParent* starting at the column *destinationColumn*.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginMoveRows`.
