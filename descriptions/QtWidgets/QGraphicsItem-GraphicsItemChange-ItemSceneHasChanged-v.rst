.. sip:enum-member-description::
    :status: todo
    :value: 16
    :digest: 0b71489c5f68a03f30f8fd4cdad4eb20

The item's scene has changed. The item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scene` is the new scene. This notification is also sent when the item is added to its initial scene, and when it is removed.The value argument is the new scene (i.e., a pointer to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`). Do not call setScene() in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. The return value is ignored.
