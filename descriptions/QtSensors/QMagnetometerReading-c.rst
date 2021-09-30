.. sip:class-description::
    :status: todo
    :brief: Represents one reading from the magnetometer
    :digest: 8e48dd18e8fc9a4f8aff961aeb66841b

The :sip:ref:`~PyQt6.QtSensors.QMagnetometerReading` class represents one reading from the magnetometer.

.. _qmagnetometerreading-qmagnetometerreading-units:

QMagnetometerReading Units
..........................

The magnetometer returns magnetic flux density values along 3 axes. The scale of the values is teslas. The axes are arranged as follows.

.. image:: ../../../images/sensors-coordinates2.jpg

The magnetometer can report on either raw magnetic flux values or geomagnetic flux values. By default it returns raw magnetic flux values. The :sip:ref:`~PyQt6.QtSensors.QMagnetometer.returnGeoValues` property must be set to return geomagnetic flux values.

The primary difference between raw and geomagnetic values is that extra processing is done to eliminate local magnetic interference from the geomagnetic values so they represent only the effect of the Earth's magnetic field. This process is not perfect and the accuracy of each reading may change.

The image below shows the difference between geomagnetic (on the left) and raw (on the right) readings for a phone that is being subjected to magnetic interference.

.. image:: ../../../images/sensors-geo-vs-raw-magnetism.jpg

The accuracy of each reading is measured as a number from 0 to 1. A value of 1 is the highest level that the device can support and 0 is the worst.

.. _qmagnetometerreading-calibration:

Calibration
...........

If the device is reporting low accuracy, then calibration might be needed before acceptable measurements can be provided. Basic calibration can usually be done by either rotating your device in a figure of eight, or by rotating the device along each of its three axes. For more information, check your device's documentation on how to calibrate the magnetic sensor.
