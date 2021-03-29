.. sip:enum-member-description::
    :status: todo
    :value: 8
    :digest: 7ab38703c165c081d71f05f3439e9f2b

The item's transformation matrix changes. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and when the item's local transformation matrix changes (i.e., as a result of calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform`. The value argument is the new matrix (i.e., a :sip:ref:`~PyQt6.QtGui.QTransform`); to get the old matrix, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`. Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform` or set any of the transformation properties in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new matrix from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`. This notification is not sent if you change the transformation properties.
