.. sip:enum-description::
    :status: todo
    :realname: Qt::ItemFlag
    :digest: f629198ec12e782d5cf6258b66b27f33

This enum describes the properties of an item:

Note that checkable items need to be given both a suitable set of flags and an initial state, indicating whether the item is checked or not. This is handled automatically for model/view components, but needs to be explicitly set for instances of QListWidgetItem, QTableWidgetItem, and QTreeWidgetItem.

Note that it is undefined behavior to reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.hasChildren` to return true for an index if that index has the  flag set.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.
