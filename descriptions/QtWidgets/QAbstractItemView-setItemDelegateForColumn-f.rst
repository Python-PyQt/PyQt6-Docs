.. sip:method-description::
    :status: todo
    :pysig: e74e0a78452c6d141f7602fa441bc0b8
    :realsig: (int,QAbstractItemDelegate*)
    :digest: 69b0c56efb1eb539d76b446edfe2c913

Sets the given item *delegate* used by this view and model for the given *column*. All items on *column* will be drawn and managed by *delegate* instead of using the default delegate (i.e., :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegate`).

Any existing column delegate for *column* will be removed, but not deleted. :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` does not take ownership of *delegate*.

**Note:** If a delegate has been assigned to both a row and a column, the row delegate will take precedence and manage the intersecting cell index.

**Warning:** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor` signal, and attempt to access, modify or close an editor that has already been closed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegateForColumn`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setItemDelegateForRow`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegate`.
