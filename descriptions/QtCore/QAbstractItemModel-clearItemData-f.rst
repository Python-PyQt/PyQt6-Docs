.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&)
    :digest: dcc0f42a5ae8b05488ec98e2e9ecfcd0

Removes the data stored in all the roles for the given *index*. Returns ``true`` if successful; otherwise returns ``false``. The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged` signal should be emitted if the data was successfully removed. The base class implementation returns ``false``

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.itemData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setItemData`.
