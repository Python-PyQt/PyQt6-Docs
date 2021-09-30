.. sip:class-description::
    :status: todo
    :brief: Represents a single hardware sensor
    :digest: c8a19a08cf6a7ef0baff3865d4e54be6

The :sip:ref:`~PyQt6.QtSensors.QSensor` class represents a single hardware sensor.

The life cycle of a sensor is typically:

* Create a sub-class of :sip:ref:`~PyQt6.QtSensors.QSensor` on the stack or heap.

* Setup as required by the application.

* Start receiving values.

* Sensor data is used by the application.

* Stop receiving values.

The sensor data is delivered via :sip:ref:`~PyQt6.QtSensors.QSensorReading` and its sub-classes.

.. _qsensor-orientation:

Orientation
-----------

Some sensors react to screen orientation changes, such as :sip:ref:`~PyQt6.QtSensors.QAccelerometer`, :sip:ref:`~PyQt6.QtSensors.QMagnetometer` and :sip:ref:`~PyQt6.QtSensors.QRotationSensor`. These are so called *orientable* sensors. For orientable sensors, :sip:ref:`~PyQt6.QtSensors.QSensor` supports changing the reporting of the reading values based on the orientation of the screen.

For orientable sensors, the :sip:ref:`~PyQt6.QtSensors.QSensor.axesOrientationMode` property controls how the orientation affects the reading values.

In the default mode, :sip:ref:`~PyQt6.QtSensors.QSensor.AxesOrientationMode.FixedOrientation`, the reading values remain unaffected by the orientation. In the :sip:ref:`~PyQt6.QtSensors.QSensor.AxesOrientationMode.AutomaticOrientation` mode, the reading values are automatically rotated by taking the current screen orientation into account. And finally, in the :sip:ref:`~PyQt6.QtSensors.QSensor.AxesOrientationMode.UserOrientation` mode, the reading values are rotated according to a user-specified orientation.

The functionality of this is only available if it is supported by the backend and if the sensor is orientable, which can be checked by calling :sip:ref:`~PyQt6.QtSensors.QSensor.isFeatureSupported` with the :sip:ref:`~PyQt6.QtSensors.QSensor.Feature.AxesOrientation` flag.

The orientation values here are always of the screen orientation, not the device orientation. The screen orientation is the orientation of the GUI. For example when rotating a device by 90 degrees counter-clockwise, the screen orientation compensates for that by rotating 90 degrees clockwise, to the effect that the GUI is still facing upright after the device has been rotated. Note that applications can lock the screen orientation, for example to force portrait or landscape mode. For locked orientations, orientable sensors will not react with reading changes if the device orientation is changed, as orientable sensors react to screen orientation changes only. This makes sense, as the purpose of orientable sensors is to keep the sensor orientation in sync with the screen orientation.

The orientation values range from 0 to 270 degrees. The orientation is applied in clockwise direction, e.g. an orientation value of 90 degrees means that the screen has been rotated 90 degress to the right from its origin position, to compensate a device rotation of 90 degrees to the left.

.. seealso:: :sip:ref:`~PyQt6.QtSensors.QSensorReading`.
