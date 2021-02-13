.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: () const
    :digest: 358befc962d7182a4d2d68aa31c9063b

Returns the region within the :sip:ref:`~PyQt6.QtGui.QScreen.availableVirtualGeometry` that this device can access.

For example a :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes` input device is fixed in place upon a single physical screen, and usually calibrated so that this area is the same as :sip:ref:`~PyQt6.QtGui.QScreen.geometry`; whereas a :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes` can probably access all screens on the virtual desktop. A Wacom graphics tablet may be configured in a way that it's mapped to all screens, or only to the screen where the user prefers to create drawings, or to the window in which drawing occurs. A :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes` device that is integrated with a touchscreen may be physically limited to that screen.

If the returned rectangle is :sip:ref:`~PyQt6.QtCore.QRect.isNull`, it means this device can access the entire virtual desktop.
