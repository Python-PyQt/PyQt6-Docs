.. sip:method-description::
    :status: todo
    :pysig: 4e64dbe4c6bc2a6e7c4518a90d337bc1
    :realsig: (QEvent::Type,const QPointingDevice*,const QPointF&,const QPointF&,qreal,float,float,float,qreal,float,Qt::KeyboardModifiers,Qt::MouseButton,Qt::MouseButtons)
    :digest: 7d72c8e0daf2b738389f3b877b9ee362

Construct a tablet event of the given *type*.

The *pos* parameter indicates where the event occurred in the widget; *globalPos* is the corresponding position in absolute coordinates.

*pressure* gives the pressure exerted on the device *dev*.

*xTilt* and *yTilt* give the device's degree of tilt from the x and y axes respectively.

*keyState* specifies which keyboard modifiers are pressed (e.g., Ctrl).

The *z* parameter gives the Z coordinate of the device on the tablet; this is usually given by a wheel on a 4D mouse. If the device does not support a Z-axis (i.e. QPointingDevice::capabilities() does not include ``ZPosition``), pass ``0`` here.

The *tangentialPressure* parameter gives the tangential pressure thumbwheel value from an airbrush. If the device does not support tangential pressure (i.e. QPointingDevice::capabilities() does not include ``TangentialPressure``), pass ``0`` here.

*rotation* gives the device's rotation in degrees. 4D mice, the Wacom Art Pen, and the Apple Pencil support rotation. If the device does not support rotation (i.e. QPointingDevice::capabilities() does not include ``Rotation``), pass ``0`` here.

The *button* that caused the event is given as a value from the :sip:ref:`~PyQt6.QtCore.Qt.MouseButton` enum. If the event *type* is not :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletPress` or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletRelease`, the appropriate button for this event is :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.NoButton`.

*buttons* is the state of all buttons at the time of the event.

.. seealso:: pos(), globalPos(), device(), :sip:ref:`~PyQt6.QtGui.QTabletEvent.pressure`, :sip:ref:`~PyQt6.QtGui.QTabletEvent.xTilt`, :sip:ref:`~PyQt6.QtGui.QTabletEvent.yTilt`, uniqueId(), :sip:ref:`~PyQt6.QtGui.QTabletEvent.rotation`, :sip:ref:`~PyQt6.QtGui.QTabletEvent.tangentialPressure`, :sip:ref:`~PyQt6.QtGui.QTabletEvent.z`.
