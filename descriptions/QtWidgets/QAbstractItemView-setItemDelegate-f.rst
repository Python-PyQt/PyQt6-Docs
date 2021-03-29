.. sip:method-description::
    :status: todo
    :pysig: 0a9c57ae6d41cc71509c5686744bb861
    :realsig: (QAbstractItemDelegate*)
    :digest: e6d0dc646a2c5606f0e1471104fff66c

Sets the item delegate for this view and its model to *delegate*. This is useful if you want complete control over the editing and display of items.

Any existing delegate will be removed, but not deleted. :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` does not take ownership of *delegate*.

**Warning:** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor` signal, and attempt to access, modify or close an editor that has already been closed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.itemDelegate`.
