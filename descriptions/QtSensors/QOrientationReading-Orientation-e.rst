.. sip:enum-description::
    :status: todo
    :digest: 628b22cdc0622aced56215f1e2b1eb55

This enum represents the orientation of the device.

To explain the meaning of each value it is helpful to refer to the following diagram.

.. image:: ../../../images/sensors-sides.jpg

The orientations are shown here in order: TopUp, TopDown, LeftUp, RightUp, FaceUp, FaceDown.

.. image:: ../../../images/sensors-orientation.jpg

It should be noted that the orientation sensor reports the orientation of the device and not the UI. The orientation of the device will not change just because the UI is rotated. This means this sensor cannot be used to detect if a device is in portrait or landscape mode.
