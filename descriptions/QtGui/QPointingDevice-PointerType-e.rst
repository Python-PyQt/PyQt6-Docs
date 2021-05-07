.. sip:enum-description::
    :status: todo
    :digest: 05ccd53d347b050161edd0bd41df41a2

This enum represents what is interacting with the pointing device.

There is some redundancy between this property and :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceType`. For example, if a touchscreen is used, then the ``DeviceType`` is ``TouchScreen`` and ``PointerType`` is ``Finger`` (always). But on a graphics tablet, it's often possible for both ends of the stylus to be used, and programs need to distinguish them. Therefore the concept is extended so that every :sip:ref:`~PyQt6.QtGui.QPointerEvent` has a , and it can simplify some event handling code to ignore the DeviceType and react differently depending on the  alone.

Valid values are:
