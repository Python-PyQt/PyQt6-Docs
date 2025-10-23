.. sip:signal-description::
    :status: todo
    :pysig: d99dd38b3a575b86dcc5a6f4e24eb135
    :realsig: (const QItemSelection&,const QItemSelection&)
    :digest: fddfbbf062b31622e516861eee61ed8a

This signal is emitted whenever the selection changes. The change in the selection is represented as an item selection of *deselected* items and an item selection of *selected* items.

Note the that the current index changes independently from the selection. Also note that this signal will not be emitted when the item model is reset.

Items which stay selected but change their index are not included in *selected* and *deselected*. Thus, this signal might be emitted with both *selected* and *deselected* empty, if only the indices of selected items change.

**Note:** It is not permitted to modify the model (e.g., by calling setData()) from within a slot connected directly to this signal. This signal may be emitted while the model is in the process of being modified, for example during row or column removal, or a model reset. Attempting to perform additional changes at such times can lead to undefined behavior. In particular, nested modifications can corrupt internal state, such as the mapping structures maintained by :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.select`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentChanged`.
