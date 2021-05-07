.. sip:method-description::
    :status: todo
    :pysig: d9db3e4f9c4b1170a57b3a029c47ace2
    :realsig: (const QPointF&,const QPointF&,QPoint,QPoint,Qt::MouseButtons,Qt::KeyboardModifiers,Qt::ScrollPhase,bool,Qt::MouseEventSource,const QPointingDevice*)
    :digest: b9a269091abec6fcd8578f3d37e4f03a

Constructs a wheel event object.

The *pos* provides the location of the mouse cursor within the window. The position in global coordinates is specified by *globalPos*.

*pixelDelta* contains the scrolling distance in pixels on screen, while *angleDelta* contains the wheel rotation angle. *pixelDelta* is optional and can be null.

The mouse and keyboard states at the time of the event are specified by *buttons* and *modifiers*.

The scrolling phase of the event is specified by *phase*, and the *source* indicates whether this is a genuine or artificial (synthesized) event.

If the system is configured to invert the delta values delivered with the event (such as natural scrolling of the touchpad on macOS), *inverted* should be ``true``. Otherwise, *inverted* is ``false``

The device from which the wheel event originated is specified by *device*.

.. seealso:: position(), globalPosition(), :sip:ref:`~PyQt6.QtGui.QWheelEvent.angleDelta`, :sip:ref:`~PyQt6.QtGui.QWheelEvent.pixelDelta`, :sip:ref:`~PyQt6.QtGui.QWheelEvent.phase`, :sip:ref:`~PyQt6.QtGui.QWheelEvent.inverted`, device().
