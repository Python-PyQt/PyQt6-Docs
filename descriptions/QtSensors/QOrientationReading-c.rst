.. sip:class-description::
    :status: todo
    :brief: Represents one reading from the orientation sensor
    :digest: 181e45180d7b603ae72c92fd31e388f4

The :sip:ref:`~PyQt6.QtSensors.QOrientationReading` class represents one reading from the orientation sensor.

The orientation sensor reports the orientation of the device. As it operates below the UI level it does not report on or even know how the UI is rotated. Most importantly this means that this sensor cannot be used to detect if a device is in portrait or landscape mode.

This sensor is useful to detect that a particular side of the device is pointing up.

.. _qorientationreading-qorientationreading-units:

QOrientationReading Units
.........................

The orientation sensor returns the orientation of the device using the pre-defined values found in the :sip:ref:`~PyQt6.QtSensors.QOrientationReading.Orientation` enum.
