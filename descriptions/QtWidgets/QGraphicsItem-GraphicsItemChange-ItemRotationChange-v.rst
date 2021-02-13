.. sip:enum-member-description::
    :status: todo
    :value: 28
    :digest: 823fefe6589f1aae97bc58edd71ed2c5

The item's rotation property changes. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and when the item's rotation property changes (i.e., as a result of calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation`). The value argument is the new rotation (i.e., a double); to get the old rotation, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`. Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new rotation from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
