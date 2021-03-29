.. sip:method-description::
    :status: todo
    :pysig: 54a5e8e51a9370586327f84486918a43
    :realsig: (const QModelIndex&,int,int,const QModelIndex&,int)
    :digest: 155d1a7086adde7f3e9d7ce833e46211

On models that support this, moves *count* columns starting with the given *sourceColumn* under parent *sourceParent* to column *destinationChild* under parent *destinationParent*.

Returns ``true`` if the columns were successfully moved; otherwise returns ``false``.

The base class implementation does nothing and returns ``false``.

If you implement your own model, you can reimplement this function if you want to support moving. Alternatively, you can provide your own API for altering the data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginMoveColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endMoveColumns`.
