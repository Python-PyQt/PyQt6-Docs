.. sip:signal-description::
    :status: todo
    :pysig: c2435248c7dc5a666882a323b22b1429
    :realsig: (const QModelIndex&,const QModelIndex&)
    :digest: 6c832f9526ff72bd86310a096f9dab59

This signal is emitted if the *current* item changes and its row is different to the row of the *previous* current item.

Note that this signal will not be emitted when the item model is reset.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentChanged`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentColumnChanged`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentIndex`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.setCurrentIndex`.
