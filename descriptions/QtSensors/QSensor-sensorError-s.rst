.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 612e6d84c53dc389b59d2a6296e9548f

This signal is emitted when an *error* code is set on the sensor. Note that some errors will cause the sensor to stop working. You should call :sip:ref:`~PyQt6.QtSensors.QSensor.isActive` to determine if the sensor is still running.
