.. sip:method-description::
    :status: todo
    :pysig: 929edda6a97571ebce7151ff0802751f
    :realsig: (int) const
    :digest: bd2057ee5c869df06f8e4a2ec31fd759

Returns the value of the property at *index*.

Note that this function is slower than calling the data function directly.

Here is an example of getting a property via the different mechanisms available.

Accessing directly provides the best performance but requires compile-time knowledge of the data you are accessing.

::

    QAccelerometerReading *reading = ...;
    qreal x = reading->x();

You can also access a property by name. To do this you must call :sip:ref:`~PyQt6.QtCore.QObject.property`.

::

    qreal x = reading->property("x").value<qreal>();

Finally, you can access values via numeric index.

::

    qreal x = reading->value(0).value<qreal>();

Note that  can only access properties declared with Q_PROPERTY() in sub-classes of :sip:ref:`~PyQt6.QtSensors.QSensorReading`.

.. seealso:: :sip:ref:`~PyQt6.QtSensors.QSensorReading.valueCount`, :sip:ref:`~PyQt6.QtCore.QObject.property`.
