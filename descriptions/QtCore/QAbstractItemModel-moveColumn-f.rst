.. sip:method-description::
    :status: todo
    :pysig: 35d5ebb71708228d3f86312cb1d8e245
    :realsig: (const QModelIndex&,int,const QModelIndex&,int)
    :digest: 888469de6ddfe117f37e56a0a3f7e90c

On models that support this, moves *sourceColumn* from *sourceParent* to *destinationChild* under *destinationParent*.

Returns ``true`` if the columns were successfully moved; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.moveColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.moveRow`.
