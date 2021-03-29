.. sip:signal-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: f28002fce7643ba95d6e48b2c52223fa

This signal is emitted after rows have been removed from the model. The removed items are those between *first* and *last* inclusive, under the given *parent* item.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveRows`.
