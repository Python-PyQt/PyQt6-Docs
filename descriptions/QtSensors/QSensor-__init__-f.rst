.. sip:method-description::
    :status: todo
    :pysig: 6c3af436f7ed26d8ee765e3f649873e6
    :realsig: (const QByteArray&,QObject*)
    :digest: 60751ba4ca869714a5586e59c048efb9

Construct the *type* sensor as a child of *parent*.

Do not use this constructor if a derived class exists for the specific sensor type.

The wrong way is to use the base class constructor:

.. literalinclude:: ../../../snippets/qtsensors-src-sensors-doc-snippets-sensors-creating.py
    :lines: 74-74

The right way is to create an instance of the derived class:

.. literalinclude:: ../../../snippets/qtsensors-src-sensors-doc-snippets-sensors-creating.py
    :lines: 67-67

The derived classes have additional properties and data members which are needed for certain features such as geo value support in :sip:ref:`~PyQt6.QtSensors.QMagnetometer` or acceleration mode support in :sip:ref:`~PyQt6.QtSensors.QAccelerometer`. These features will only work properly when creating a sensor instance from a :sip:ref:`~PyQt6.QtSensors.QSensor` subclass.

Only use this constructor if there is no derived sensor class available. Note that all built-in sensors have a derived class, so using this constructor should only be necessary when implementing custom sensors.
