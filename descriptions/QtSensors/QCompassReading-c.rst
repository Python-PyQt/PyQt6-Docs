.. sip:class-description::
    :status: todo
    :brief: Represents one reading from a compass
    :digest: 3b8b76de065a7657823f600c61da9487

The :sip:ref:`~PyQt6.QtSensors.QCompassReading` class represents one reading from a compass.

.. _qcompassreading-qcompassreading-units:

QCompassReading Units
.....................

The compass returns the azimuth of the device as degrees from magnetic north in a clockwise direction based on the top of the device, as defined by :sip:ref:`~PyQt6.QtGui.QScreen.nativeOrientation`. There is also a value to indicate the calibration status of the device. If the device is not calibrated the azimuth may not be accurate.

Digital compasses are susceptible to magnetic interference and may need calibration after being placed near anything that emits a magnetic force. Accuracy of the compass can be affected by any ferrous materials that are nearby.

The calibration status of the device is measured as a number from 0 to 1. A value of 1 is the highest level that the device can support and 0 is the worst.
