.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: e9b5b521de7cd3245b6f631da799e851

Hides the item if *hide* is true, otherwise shows the item.

**Note:** A call to this function has no effect if the item is not currently in a view. In particular, calling ``setHidden(true)`` on an item and only then adding it to a view will result in a visible item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.isHidden`.
