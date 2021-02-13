.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1c49fb5833615365badb041690d12f83

Takes keyboard input focus from the item.

If it has focus, a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusOutEvent` is sent to this item to tell it that it is about to lose the focus.

Only items that set the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsFocusable` flag, or widgets that set an appropriate focus policy, can accept keyboard focus.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.focusPolicy`.
