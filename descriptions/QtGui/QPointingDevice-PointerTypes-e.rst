.. sip:enum-description::
    :status: todo
    :realname: QPointingDevice::PointerType
    :digest: 355db3dfe09d2ee1d480b3465488b2ba

This enum represents what is interacting with the pointing device.

There is some redundancy between this property and :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes`. For example, if a touchscreen is used, then the ``DeviceType`` is ``TouchScreen`` and ``PointerType`` is ``Finger`` (always). But on a graphics tablet, it's often possible for both ends of the stylus to be used, and programs need to distinguish them. Therefore the concept is extended so that every :sip:ref:`~PyQt6.QtGui.QPointerEvent` has a , and it can simplify some event handling code to ignore the :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes.DeviceType` and react differently depending on the  alone.

Valid values are:
