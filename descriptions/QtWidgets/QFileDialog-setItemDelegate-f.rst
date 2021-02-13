.. sip:method-description::
    :status: todo
    :pysig: 0a9c57ae6d41cc71509c5686744bb861
    :realsig: (QAbstractItemDelegate*)
    :digest: c25ac8cc5ad097fe5485a2a1411b074b

Sets the item delegate used to render items in the views in the file dialog to the given *delegate*.

Any existing delegate will be removed, but not deleted. :sip:ref:`~PyQt6.QtWidgets.QFileDialog` does not take ownership of *delegate*.

**Warning:** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor` signal, and attempt to access, modify or close an editor that has already been closed.

Note that the model used is :sip:ref:`~PyQt6.QtGui.QFileSystemModel`. It has custom item data roles, which is described by the :sip:ref:`~PyQt6.QtGui.QFileSystemModel.Roles` enum. You can use a :sip:ref:`~PyQt6.QtWidgets.QFileIconProvider` if you only want custom icons.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.itemDelegate`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setIconProvider`, :sip:ref:`~PyQt6.QtGui.QFileSystemModel`.
