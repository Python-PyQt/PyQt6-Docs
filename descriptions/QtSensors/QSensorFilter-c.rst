.. sip:class-description::
    :status: todo
    :brief: Efficient callback facility for asynchronous notifications of sensor changes
    :digest: 2531cd29beb10fcbbb3cda8be4019301

The :sip:ref:`~PyQt6.QtSensors.QSensorFilter` class provides an efficient callback facility for asynchronous notifications of sensor changes.

Some sensors (eg. the accelerometer) are often accessed very frequently. This may be slowed down by the use of signals and slots. The :sip:ref:`~PyQt6.QtSensors.QSensorFilter` interface provides a more efficient way for the sensor to notify your class that the sensor has changed.

Additionally, multiple filters can be added to a sensor. They are called in order and each filter has the option to modify the values in the reading or to suppress the reading altogether.

Note that the values in the class returned by :sip:ref:`~PyQt6.QtSensors.QSensor.reading` will not be updated until after the filters have been run.

.. seealso:: :sip:ref:`~PyQt6.QtSensors.QSensorFilter.filter`.
