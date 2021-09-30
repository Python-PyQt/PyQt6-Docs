.. sip:signal-description::
    :status: todo
    :pysig: d99dd38b3a575b86dcc5a6f4e24eb135
    :realsig: (const QItemSelection&,const QItemSelection&)
    :digest: b4625a6baea42ba8176b4bf861eb24d2

This signal is emitted whenever the selection changes. The change in the selection is represented as an item selection of *deselected* items and an item selection of *selected* items.

Note the that the current index changes independently from the selection. Also note that this signal will not be emitted when the item model is reset.

Items which stay selected but change their index are not included in *selected* and *deselected*. Thus, this signal might be emitted with both *selected* and *deselected* empty, if only the indices of selected items change.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.select`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentChanged`.
