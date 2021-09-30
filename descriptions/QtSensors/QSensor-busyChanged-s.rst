.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 17ad03fe962fab113b1636e821b79ac5

This signal is emitted when the sensor is no longer busy. This can be used to grab a sensor when it becomes available.

::

    sensor.start();
    if (sensor.isBusy()) {
        // need to wait for busyChanged signal and try again
    }
