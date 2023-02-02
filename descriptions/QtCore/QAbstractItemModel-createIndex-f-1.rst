.. sip:method-description::
    :status: todo
    :pysig: 3de2092b5d8358d15efdbe835a785e89
    :realsig: (int,int,const void*) const
    :digest: f086121e60882e75e09af3b7e1a52072

Creates a model index for the given *row* and *column* with the internal pointer *ptr*.

When using a :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel`, its indexes have their own internal pointer. It is not advisable to access this internal pointer outside of the model. Use the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` function instead.

This function provides a consistent interface that model subclasses must use to create model indexes.
