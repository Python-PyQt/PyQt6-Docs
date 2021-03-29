.. sip:method-description::
    :status: todo
    :pysig: d4492a13818022be6671f3a7fc12bcaa
    :realsig: (QWidget*,const QModelIndex&) const
    :digest: cb8bd0c4a744ef036a56d24ef820fa49

Sets the contents of the given *editor* to the data for the item at the given *index*. Note that the index contains information about the model being used.

The base implementation does nothing. If you want custom editing you will need to reimplement this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setModelData`.
