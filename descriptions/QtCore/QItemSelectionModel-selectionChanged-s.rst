.. sip:signal-description::
    :status: todo
    :pysig: d99dd38b3a575b86dcc5a6f4e24eb135
    :realsig: (const QItemSelection&,const QItemSelection&)
    :digest: e5d8c657ab3ac0b4dea030ab150cf37b

This signal is emitted whenever the selection changes. The change in the selection is represented as an item selection of *deselected* items and an item selection of *selected* items.

Note the that the current index changes independently from the selection. Also note that this signal will not be emitted when the item model is reset.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.select`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentChanged`.
