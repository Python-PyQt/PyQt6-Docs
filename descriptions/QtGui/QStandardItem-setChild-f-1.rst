.. sip:method-description::
    :status: todo
    :pysig: d150e81fdb6bbf67b4af75a24beb372e
    :realsig: (int,int,QStandardItem*)
    :digest: 79761e498d52c4caa201310991ed0055

Sets the child item at (\ *row*, *column*) to *item*. This item (the parent item) takes ownership of *item*. If necessary, the row count and column count are increased to fit the item.

**Note:** Passing ``nullptr`` as *item* removes the item.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.child`.
