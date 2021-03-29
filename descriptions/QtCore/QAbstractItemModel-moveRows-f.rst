.. sip:method-description::
    :status: todo
    :pysig: 54a5e8e51a9370586327f84486918a43
    :realsig: (const QModelIndex&,int,int,const QModelIndex&,int)
    :digest: 99c0d7aaba7d4051f0f28e44390ebc10

On models that support this, moves *count* rows starting with the given *sourceRow* under parent *sourceParent* to row *destinationChild* under parent *destinationParent*.

Returns ``true`` if the rows were successfully moved; otherwise returns ``false``.

The base class implementation does nothing and returns ``false``.

If you implement your own model, you can reimplement this function if you want to support moving. Alternatively, you can provide your own API for altering the data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginMoveRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endMoveRows`.
