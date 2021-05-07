.. sip:method-description::
    :status: todo
    :pysig: 54325e9368999a85b6b186618ee81876
    :realsig: () const
    :digest: 854c6342668d1b8bd653ccbaa35525be

Returns the mouse buttons that this item accepts mouse events for. By default, all mouse buttons are accepted.

If an item accepts a mouse button, it will become the mouse grabber item when a mouse press event is delivered for that mouse button. However, if the item does not accept the button, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will forward the mouse events to the first item beneath it that does.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptedMouseButtons`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`.
