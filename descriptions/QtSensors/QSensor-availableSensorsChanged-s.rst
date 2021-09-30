.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7c02a1888ace6681eb3dfd398c0b66a7

This signal is emitted when the list of available sensors has changed. The sensors available to a program will not generally change over time however some of the available sensors may represent hardware that is not permanently connected. For example, a game controller that is connected via bluetooth would become available when it was on and would become unavailable when it was off.

.. seealso:: :sip:ref:`~PyQt6.QtSensors.QSensor.sensorTypes`, :sip:ref:`~PyQt6.QtSensors.QSensor.sensorsForType`.
