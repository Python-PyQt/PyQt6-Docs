.. sip:method-description::
    :status: todo
    :pysig: 70fdb46d124e02d8a4f903d26e7c1cfc
    :realsig: (const QPointF&) const
    :digest: 26a0330f959580163ad14dd90c8ff21d

Returns ``true`` if this item contains *point*, which is in local coordinates; returns ``false`` otherwise.

This function can be overridden in order to handle point collisions in items with custom shapes. The default implementation checks whether the point is inside :sip:ref:`~PyQt6.QtQuick.QQuickItem.containmentMask` if it is set, or inside the bounding box otherwise.

**Note:** This method is used for hit-testing each :sip:ref:`~PyQt6.QtGui.QEventPoint` during event delivery, so the implementation should be kept as lightweight as possible.
