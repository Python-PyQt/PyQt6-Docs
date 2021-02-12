.. sip:method-description::
    :status: todo
    :pysig: 68069430c93714918cd687ed868d9a98
    :realsig: (const QModelIndex&,const QMap<int,QVariant>&)
    :digest: 59f0a21df7e7c73aca709beee25f5a50

Sets the role data for the item at *index* to the associated value in *roles*, for every :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`.

Returns ``true`` if successful; otherwise returns ``false``.

Roles that are not in *roles* will not be modified.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.itemData`.
