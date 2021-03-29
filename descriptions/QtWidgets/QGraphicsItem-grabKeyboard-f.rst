.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5f356203d2d507c6d080d20f467f1837

Grabs the keyboard input.

The item will receive all keyboard input to the scene until one of the following events occur:

* The item becomes invisible

* The item is removed from the scene

* The item is deleted

* The item calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabKeyboard`

* Another item calls ; the item will regain the keyboard grab when the other item calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabKeyboard`.

When an item gains the keyboard grab, it receives a :sip:ref:`~PyQt6.QtCore.QEvent.Type.GrabKeyboard` event. When it loses the keyboard grab, it receives a :sip:ref:`~PyQt6.QtCore.QEvent.Type.UngrabKeyboard` event. These events can be used to detect when your item gains or loses the keyboard grab through other means than gaining input focus.

It is almost never necessary to explicitly grab the keyboard in Qt, as Qt grabs and releases it sensibly. In particular, Qt grabs the keyboard when your item gains input focus, and releases it when your item loses input focus, or when the item is hidden.

Note that only visible items can grab keyboard input. Calling  on an invisible item has no effect.

Keyboard events are not affected.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.ungrabKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.grabMouse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFocus`.
