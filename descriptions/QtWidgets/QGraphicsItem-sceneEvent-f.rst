.. sip:method-description::
    :status: todo
    :pysig: 78c2ee29b9f6bed2b9f05a748c095133
    :realsig: (QEvent*)
    :digest: 7b98c9928103a47c884c3467c6b1d686

This virtual function receives events to this item. Reimplement this function to intercept events before they are dispatched to the specialized event handlers :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contextMenuEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusInEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverLeaveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.keyPressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.keyReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseDoubleClickEvent`.

Returns ``true`` if the event was recognized and handled; otherwise, (e.g., if the event type was not recognized,) false is returned.

*event* is the intercepted event.
