.. sip:signal-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: cea8118d39ebe2b7b97e77e90cf7cddf

This signal is emitted just before columns are removed from the model. The items to be removed are those between *first* and *last* inclusive, under the given *parent* item.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveColumns`.
