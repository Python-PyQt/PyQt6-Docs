.. sip:method-description::
    :status: todo
    :pysig: c2435248c7dc5a666882a323b22b1429
    :realsig: (const QModelIndex&,const QModelIndex&)
    :digest: 4713fc3116b33ad0e721a1e6ffccdd65

This slot is called when a new item becomes the current item. The previous current item is specified by the *previous* index, and the new item by the *current* index.

If you want to know about changes to items see the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.dataChanged` signal.
