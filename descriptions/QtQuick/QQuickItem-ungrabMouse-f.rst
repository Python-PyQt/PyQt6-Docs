.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: eeabb212daad5e9599c06da6b7aa0dd9

Use QPointerEvent::setExclusiveGrabber()

Releases the mouse grab following a call to :sip:ref:`~PyQt6.QtQuick.QQuickItem.grabMouse`.

Note that this function should only be called when the item wants to stop handling further events. There is no need to call this function after a release or cancel event since no future events will be received in any case. No move or release events will be delivered after this function was called.
