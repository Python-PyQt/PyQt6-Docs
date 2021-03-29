.. sip:method-description::
    :status: todo
    :pysig: af193f7da54d4df813f044d1a85c747b
    :realsig: (const QModelIndex&)
    :digest: a0c5a28091d0f0c434edf2649c8a8ec6

Sets the current item to be the item at *index*.

Unless the current selection mode is :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.SelectionMode.NoSelection`, the item is also selected. Note that this function also updates the starting position for any new selections the user performs.

To set an item as the current item without selecting it, call

``selectionModel()->setCurrentIndex(index, QItemSelectionModel::NoUpdate);``

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.currentIndex`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.currentChanged`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionMode`.
