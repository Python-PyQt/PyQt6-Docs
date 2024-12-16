.. sip:method-description::
    :status: todo
    :pysig: 512e449d5e1d80af40a0b07753eaa671
    :realsig: (const QModelIndex&, const QMap<int, QVariant>&)
    :digest: 59f0a21df7e7c73aca709beee25f5a50

Sets the role data for the item at *index* to the associated value in *roles*, for every :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`.

Returns ``true`` if successful; otherwise returns ``false``.

Roles that are not in *roles* will not be modified.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.itemData`.
