.. sip:method-description::
    :status: todo
    :pysig: d2a61dc4dc1606476b5f920dc772dfe2
    :realsig: (const QModelIndex&) const
    :digest: 2e6dad0399a403ee387a94da5e4a8e75

Returns a map with values for all predefined roles in the model for the item at the given *index*.

Reimplement this function if you want to extend the default behavior of this function to include custom roles in the map.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setItemData`, :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`.
