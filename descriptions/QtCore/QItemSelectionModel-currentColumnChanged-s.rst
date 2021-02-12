.. sip:signal-description::
    :status: todo
    :pysig: c2435248c7dc5a666882a323b22b1429
    :realsig: (const QModelIndex&,const QModelIndex&)
    :digest: a147aca4a226e2da2e46b7ca52e45c29

This signal is emitted if the *current* item changes and its column is different to the column of the *previous* current item.

Note that this signal will not be emitted when the item model is reset.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentChanged`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentRowChanged`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentIndex`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.setCurrentIndex`.
