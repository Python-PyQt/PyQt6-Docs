.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fe4aa20b9a1e341b52f106b4ba554446

Use QPointerEvent::setExclusiveGrabber()

Grabs the mouse input.

This item will receive all mouse events until :sip:ref:`~PyQt6.QtQuick.QQuickItem.ungrabMouse` is called. Usually this function should not be called, since accepting for example a mouse press event makes sure that the following events are delivered to the item. If an item wants to take over mouse events from the current receiver, it needs to call this function.

**Warning:** This function should be used with caution.
