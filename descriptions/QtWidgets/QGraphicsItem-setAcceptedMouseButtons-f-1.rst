.. sip:method-description::
    :status: todo
    :pysig: 54325e9368999a85b6b186618ee81876
    :realsig: (Qt::MouseButtons)
    :digest: 5d1768815436059ef1779dc1d0aad793

Sets the mouse *buttons* that this item accepts mouse events for.

By default, all mouse buttons are accepted. If an item accepts a mouse button, it will become the mouse grabber item when a mouse press event is delivered for that button. However, if the item does not accept the mouse button, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will forward the mouse events to the first item beneath it that does.

To disable mouse events for an item (i.e., make it transparent for mouse events), call setAcceptedMouseButtons(\ :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.NoButton`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptedMouseButtons`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`.
