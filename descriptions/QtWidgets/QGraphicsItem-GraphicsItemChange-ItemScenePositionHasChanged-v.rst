.. sip:enum-member-description::
    :status: todo
    :value: 27
    :digest: 0d5dff1e1cae4020e71cff2b2841ad0e

The item's scene position has changed. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsScenePositionChanges` flag is enabled, and after the item's scene position has changed (i.e., the position or transformation of the item itself or the position or transformation of any ancestor has changed). The value argument is the new scene position (the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scenePos`), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` ignores the return value for this notification (i.e., a read-only notification).
