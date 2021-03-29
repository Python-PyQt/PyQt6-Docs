.. sip:method-description::
    :status: todo
    :pysig: e74e0a78452c6d141f7602fa441bc0b8
    :realsig: (int,QAbstractItemDelegate*)
    :digest: e4acd85e138123a60afe5fe7867bd676

Sets the given item *delegate* used by this view and model for the given *row*. All items on *row* will be drawn and managed by *delegate* instead of using the default delegate (i.e., :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegate`).

Any existing row delegate for *row* will be removed, but not deleted. :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` does not take ownership of *delegate*.

**Note:** If a delegate has been assigned to both a row and a column, the row delegate (i.e., this delegate) will take precedence and manage the intersecting cell index.

**Warning:** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor` signal, and attempt to access, modify or close an editor that has already been closed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegateForRow`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setItemDelegateForColumn`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegate`.
