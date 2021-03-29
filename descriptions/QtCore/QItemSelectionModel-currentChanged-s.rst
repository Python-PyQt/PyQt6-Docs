.. sip:signal-description::
    :status: todo
    :pysig: c2435248c7dc5a666882a323b22b1429
    :realsig: (const QModelIndex&,const QModelIndex&)
    :digest: 971d3360fd2ffdf47981a085697920ff

This signal is emitted whenever the current item changes. The *previous* model item index is replaced by the *current* index as the selection's current item.

Note that this signal will not be emitted when the item model is reset.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentIndex`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.setCurrentIndex`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.selectionChanged`.
