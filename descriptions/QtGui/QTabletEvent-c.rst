.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a Tablet event
    :digest: 4413593d72c7b77b44eec37f000763a1

The :sip:ref:`~PyQt6.QtGui.QTabletEvent` class contains parameters that describe a Tablet event.

*Tablet events* are generated from tablet peripherals such as Wacom tablets and various other brands, and electromagnetic stylus devices included with some types of tablet computers. (It is not the same as :sip:ref:`~PyQt6.QtGui.QTouchEvent` which a touchscreen generates, even when a passive stylus is used on a touchscreen.)

Tablet events are similar to mouse events; for example, the x(), y(), pos(), globalX(), globalY(), and globalPos() accessors provide the cursor position, and you can see which buttons() are pressed (pressing the stylus tip against the tablet surface is equivalent to a left mouse button). But tablet events also pass through some extra information that the tablet device driver provides; for example, you might want to do subpixel rendering with higher resolution coordinates (globalPosF()), adjust color brightness based on the :sip:ref:`~PyQt6.QtGui.QTabletEvent.pressure` of the tool against the tablet surface, use different brushes depending on the type of tool in use (deviceType()), modulate the brush shape in some way according to the X-axis and Y-axis tilt of the tool with respect to the tablet surface (\ :sip:ref:`~PyQt6.QtGui.QTabletEvent.xTilt` and :sip:ref:`~PyQt6.QtGui.QTabletEvent.yTilt`), and use a virtual eraser instead of a brush if the user switches to the other end of a double-ended stylus (pointerType()).

Every event contains an accept flag that indicates whether the receiver wants the event. You should call QTabletEvent::accept() if you handle the tablet event; otherwise it will be sent to the parent widget. The exception are TabletEnterProximity and TabletLeaveProximity events: these are only sent to :sip:ref:`~PyQt6.QtWidgets.QApplication` and do not check whether or not they are accepted.

The :sip:ref:`~PyQt6.QtWidgets.QWidget.setEnabled` function can be used to enable or disable mouse, tablet and keyboard events for a widget.

The event handler :sip:ref:`~PyQt6.QtWidgets.QWidget.tabletEvent` receives TabletPress, TabletRelease and TabletMove events. Qt will first send a tablet event, then if it is not accepted by any widget, it will send a mouse event. This allows users of applications that are not designed for tablets to use a tablet like a mouse. However high-resolution drawing applications should handle the tablet events, because they can occur at a higher frequency, which is a benefit for smooth and accurate drawing. If the tablet events are rejected, the synthetic mouse events may be compressed for efficiency.

Note that pressing the stylus button while the stylus hovers over the tablet will generate a button press on some types of tablets, while on other types it will be necessary to press the stylus against the tablet surface in order to register the simultaneous stylus button press.

.. _qtabletevent-notes-for-x11-users:

Notes for X11 Users
-------------------

If the tablet is configured in xorg.conf to use the Wacom driver, there will be separate XInput "devices" for the stylus, eraser, and (optionally) cursor and touchpad. Qt recognizes these by their names. Otherwise, if the tablet is configured to use the evdev driver, there will be only one device and applications may not be able to distinguish the stylus from the eraser.

.. _qtabletevent-notes-for-windows-users:

Notes for Windows Users
-----------------------

Tablet support currently requires the WACOM windows driver providing the DLL ``wintab32.dll`` to be installed. It is contained in older packages, for example ``pentablet_5.3.5-3.exe``.
