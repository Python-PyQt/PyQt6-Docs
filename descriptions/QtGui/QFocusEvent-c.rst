.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for widget focus events
    :digest: eeb3c1aaa2289a5be93e81afec49336d

The :sip:ref:`~PyQt6.QtGui.QFocusEvent` class contains event parameters for widget focus events.

Focus events are sent to widgets when the keyboard input focus changes. Focus events occur due to mouse actions, key presses (such as Tab or Backtab), the window system, popup menus, keyboard shortcuts, or other application-specific reasons. The reason for a particular focus event is returned by :sip:ref:`~PyQt6.QtGui.QFocusEvent.reason` in the appropriate event handler.

The event handlers QWidget::focusInEvent(), QWidget::focusOutEvent(), QGraphicsItem::focusInEvent and QGraphicsItem::focusOutEvent() receive focus events.

.. seealso:: QWidget::setFocus()QWidget::setFocusPolicy()Keyboard Focus in Widgets.
