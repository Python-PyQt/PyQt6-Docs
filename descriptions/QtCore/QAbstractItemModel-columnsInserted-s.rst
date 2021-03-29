.. sip:signal-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: 287e51b8f114f3e1711ef21ebb4eaa9c

This signal is emitted after columns have been inserted into the model. The new items are those between *first* and *last* inclusive, under the given *parent* item.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertColumns`.
