.. sip:method-description::
    :status: todo
    :pysig: 35d5ebb71708228d3f86312cb1d8e245
    :realsig: (const QModelIndex&,int,const QModelIndex&,int)
    :digest: 2193b31165e6aeaf8c8527a94fac8019

On models that support this, moves *sourceRow* from *sourceParent* to *destinationChild* under *destinationParent*.

Returns ``true`` if the rows were successfully moved; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.moveRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.moveColumn`.
