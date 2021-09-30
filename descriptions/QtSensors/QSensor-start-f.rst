.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: b563b7d6c8548b6e1059d1f7ef9b4c08

Start retrieving values from the sensor. Returns true if the sensor was started, false otherwise.

The sensor may fail to start for several reasons.

Once an application has started a sensor it must wait until the sensor receives a new value before it can query the sensor's values. This is due to how the sensor receives values from the system. Sensors do not (in general) poll for new values, rather new values are pushed to the sensors as they happen.

For example, this code will not work as intended.

::

    sensor->start();
    sensor->reading()->x(); // no data available

To work correctly, the code that accesses the reading should ensure the :sip:ref:`~PyQt6.QtSensors.QSensor.readingChanged` signal has been emitted.

::

        connect(sensor, SIGNAL(readingChanged()), this, SLOT(checkReading()));
        sensor->start();
    }
    void MyClass::checkReading() {
        sensor->reading()->x();

.. seealso:: QSensor::busy.
