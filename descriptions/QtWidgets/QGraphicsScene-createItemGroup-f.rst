.. sip:method-description::
    :status: todo
    :pysig: f87fd8117baa25341890eac93c35f62d
    :realsig: (const QList<QGraphicsItem*>&)
    :digest: 4446cbc41c96c3ecc00b2eb5671ca921

Groups all items in *items* into a new :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup`, and returns a pointer to the group. The group is created with the common ancestor of *items* as its parent, and with position (0, 0). The items are all reparented to the group, and their positions and transformations are mapped to the group. If *items* is empty, this function will return an empty top-level :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` has ownership of the group item; you do not need to delete it. To dismantle (ungroup) a group, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.destroyItemGroup`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.destroyItemGroup`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.addToGroup`.
