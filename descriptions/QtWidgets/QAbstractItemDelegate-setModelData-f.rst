.. sip:method-description::
    :status: todo
    :pysig: 6fadfd1a02613ebb16f7304e7dd3f74a
    :realsig: (QWidget*,QAbstractItemModel*,const QModelIndex&) const
    :digest: 3b457cf8339f9ef66a67fc5e75d07c35

Sets the data for the item at the given *index* in the *model* to the contents of the given *editor*.

The base implementation does nothing. If you want custom editing you will need to reimplement this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setEditorData`.
