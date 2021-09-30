.. sip:class-description::
    :status: todo
    :brief: Holds readings from the humidity sensor
    :digest: c4f99eace2c0d5e02d049878627562fa

The :sip:ref:`~PyQt6.QtSensors.QHumidityReading` class holds readings from the humidity sensor.

.. _qhumidityreading-qhumidityreading-units:

QHumidityReading Units
......................

The humidity sensor returns the relative humidity as a percentage, and absolute humidity in grams per cubic meter (g/m3). Note that some sensors may not support absolute humidity, 0 will be returned in this case.
