.. sip:class-description::
    :status: todo
    :brief: Convenience wrapper around QSensor
    :digest: 5f7ed18ccbe102dd2b109ca9e81fd861

The :sip:ref:`~PyQt6.QtSensors.QAccelerometer` class is a convenience wrapper around :sip:ref:`~PyQt6.QtSensors.QSensor`.

The only behavioural difference is that this class sets the type properly.

It also supports changing the acceleration mode, which controls whether the force of gravity is included in the accelerometer values or not.

Furthermore, this class features a :sip:ref:`~PyQt6.QtSensors.QAccelerometer.reading` function that returns a :sip:ref:`~PyQt6.QtSensors.QAccelerometerReading` instead of a :sip:ref:`~PyQt6.QtSensors.QSensorReading`.

For details about how the sensor works, see :sip:ref:`~PyQt6.QtSensors.QAccelerometerReading`.

.. seealso:: :sip:ref:`~PyQt6.QtSensors.QAccelerometerReading`.
