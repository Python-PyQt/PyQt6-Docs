.. sip:method-description::
    :status: todo
    :pysig: 30985e3a4dd64cc7ba58e0a7032868a2
    :realsig: (const QList<int>&)
    :digest: 8c53c5181f4262673150f5167375fe91

Use QPointerEvent::setExclusiveGrabber(). Grabs the touch points specified by *ids*.

These touch points will be owned by the item until they are released. Alternatively, the grab can be stolen by a filtering item like Flickable. Use :sip:ref:`~PyQt6.QtQuick.QQuickItem.setKeepTouchGrab` to prevent the grab from being stolen.
