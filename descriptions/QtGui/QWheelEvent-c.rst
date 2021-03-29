.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a wheel event
    :digest: a62c6767fdabe6db41ef3cdaf044863e

The :sip:ref:`~PyQt6.QtGui.QWheelEvent` class contains parameters that describe a wheel event.

Wheel events are sent to the widget under the mouse cursor, but if that widget does not handle the event they are sent to the focus widget. Wheel events are generated for both mouse wheels and trackpad scroll gestures. There are two ways to read the wheel event delta: :sip:ref:`~PyQt6.QtGui.QWheelEvent.angleDelta` returns the deltas in wheel degrees. These values are always provided. :sip:ref:`~PyQt6.QtGui.QWheelEvent.pixelDelta` returns the deltas in screen pixels, and is available on platforms that have high-resolution trackpads, such as macOS. If that is the case, device()->type() will return QInputDevice::DeviceType::Touchpad.

The functions position() and globalPosition() return the mouse cursor's location at the time of the event.

A wheel event contains a special accept flag that indicates whether the receiver wants the event. You should call ignore() if you do not handle the wheel event; this ensures that it will be sent to the parent widget.

The :sip:ref:`~PyQt6.QtWidgets.QWidget.setEnabled` function can be used to enable or disable mouse and keyboard events for a widget.

The event handler :sip:ref:`~PyQt6.QtWidgets.QWidget.wheelEvent` receives wheel events.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMouseEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabMouse`.
