.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (QGraphicsItem*)
    :digest: c1f2357eb6791eedaf6a9edb2db88142

Sets this item's parent item to *newParent*. If this item already has a parent, it is first removed from the previous parent. If *newParent* is 0, this item will become a top-level item.

Note that this implicitly adds this graphics item to the scene of the parent. You should not :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem` the item to the scene yourself.

The behavior when calling this function on an item that is an ancestor of *newParent* is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.parentItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.childItems`.
