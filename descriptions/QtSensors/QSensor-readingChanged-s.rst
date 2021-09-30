.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 31159f95e6041d3f68adb048fb7088d7

This signal is emitted when a new sensor reading is received.

The sensor reading can be found in the :sip:ref:`~PyQt6.QtSensors.QSensor.reading` property. Note that the reading object is a volatile cache of the most recent sensor reading that has been received so the application should process the reading immediately or save the values somewhere for later processing.

Before this signal has been emitted for the first time, the reading object will have uninitialized data.

.. seealso:: :sip:ref:`~PyQt6.QtSensors.QSensor.start`.
