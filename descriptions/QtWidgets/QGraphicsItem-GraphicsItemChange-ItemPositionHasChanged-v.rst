.. sip:enum-member-description::
    :status: todo
    :value: 9
    :digest: de05d5b20bae69f070a9eabed2d0d3f6

The item's position has changed. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and after the item's local position, relative to its parent, has changed. The value argument is the new position (the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.pos`), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` ignores the return value for this notification (i.e., a read-only notification).
