.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f8dd904e50b3d90d12e95097458cbddd

Grabs the mouse input.

This item will receive all mouse events for the scene until any of the following events occurs:

* The item becomes invisible

* The item is removed from the scene

* The item is deleted

* The item call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabMouse`

* Another item calls ; the item will regain the mouse grab when the other item calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabMouse`.

When an item gains the mouse grab, it receives a :sip:ref:`~PyQt6.QtCore.QEvent.Type.GrabMouse` event. When it loses the mouse grab, it receives a :sip:ref:`~PyQt6.QtCore.QEvent.Type.UngrabMouse` event. These events can be used to detect when your item gains or loses the mouse grab through other means than receiving mouse button events.

It is almost never necessary to explicitly grab the mouse in Qt, as Qt grabs and releases it sensibly. In particular, Qt grabs the mouse when you press a mouse button, and keeps the mouse grabbed until you release the last mouse button. Also, :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Popup` widgets implicitly call  when shown, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabMouse` when hidden.

Note that only visible items can grab mouse input. Calling  on an invisible item has no effect.

Keyboard events are not affected.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mouseGrabberItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabMouse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.grabKeyboard`.
