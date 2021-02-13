.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a mouse event
    :digest: 4837e13e3449c74206b951ce438b8ce8

The :sip:ref:`~PyQt6.QtGui.QMouseEvent` class contains parameters that describe a mouse event.

Mouse events occur when a mouse button is pressed or released inside a widget, or when the mouse cursor is moved.

Mouse move events will occur only when a mouse button is pressed down, unless mouse tracking has been enabled with QWidget::setMouseTracking().

Qt automatically grabs the mouse when a mouse button is pressed inside a widget; the widget will continue to receive mouse events until the last mouse button is released.

A mouse event contains a special accept flag that indicates whether the receiver wants the event. You should call ignore() if the mouse event is not handled by your widget. A mouse event is propagated up the parent widget chain until a widget accepts it with accept(), or an event filter consumes it.

**Note:** If a mouse event is propagated to a widget for which :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_NoMousePropagation` has been set, that mouse event will not be propagated further up the parent widget chain.

The state of the keyboard modifier keys can be found by calling the :sip:ref:`~PyQt6.QtGui.QInputEvent.modifiers` function, inherited from :sip:ref:`~PyQt6.QtGui.QInputEvent`.

The position() function gives the cursor position relative to the widget or item that receives the mouse event. If you move the widget as a result of the mouse event, use the global position returned by globalPosition() to avoid a shaking motion.

The QWidget::setEnabled() function can be used to enable or disable mouse and keyboard events for a widget.

Reimplement the QWidget event handlers, QWidget::mousePressEvent(), QWidget::mouseReleaseEvent(), QWidget::mouseDoubleClickEvent(), and QWidget::mouseMoveEvent() to receive mouse events in your own widgets.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QCursor.pos`, QWidget::setMouseTracking()QWidget::grabMouse().
