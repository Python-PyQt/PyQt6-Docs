.. sip:enum-description::
    :status: todo
    :digest: 74f4cfc2ee4961abf1d3641271fb57cb

This enum represents the orientation of the device.

To explain the meaning of each value it is helpful to refer to the following diagram.

.. image:: ../../../images/sensors-sides.jpg

The orientations are shown here in order: , , , , , .

.. image:: ../../../images/sensors-orientation.jpg

It should be noted that the orientation sensor reports the orientation of the device and not the UI. The orientation of the device will not change just because the UI is rotated. This means this sensor cannot be used to detect if a device is in portrait or landscape mode.
