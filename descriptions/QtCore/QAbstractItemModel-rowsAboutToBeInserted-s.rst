.. sip:signal-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: fe74c407cf699c975e0cbcb44699f400

This signal is emitted just before rows are inserted into the model. The new items will be positioned between *start* and *end* inclusive, under the given *parent* item.

**Note:** Components connected to this signal use it to adapt to changes in the model's dimensions. It can only be emitted by the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation, and cannot be explicitly emitted in subclass code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertRows`.
