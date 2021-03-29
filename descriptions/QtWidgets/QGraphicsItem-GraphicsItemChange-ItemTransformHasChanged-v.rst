.. sip:enum-member-description::
    :status: todo
    :value: 10
    :digest: d514a585dda600a1fbdc7fc123250b9a

The item's transformation matrix has changed either because :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform` is called, or one of the transformation properties is changed. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and after the item's local transformation matrix has changed. The value argument is the new matrix (same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` ignores the return value for this notification (i.e., a read-only notification).
