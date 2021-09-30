.. sip:method-description::
    :status: todo
    :pysig: dc2dfd9d32d0130bf9b467604eaa0dd7
    :realsig: (QSensor::Feature) const
    :digest: 8a94295f6a352bda466035446599b683

Checks if a specific feature is supported by the backend.

`QtSensors <https://doc.qt.io/qt-6/qtsensors-qmlmodule.html>`_ supports a rich API for controlling and providing information about sensors. Naturally, not all of this functionality can be supported by all of the backends.

To check if the current backend supports the feature *feature*, call this function.

The backend needs to be connected, otherwise false will be returned. Calling :sip:ref:`~PyQt6.QtSensors.QSensor.connectToBackend` or :sip:ref:`~PyQt6.QtSensors.QSensor.start` will create a connection to the backend.

Backends have to implement QSensorBackend::isFeatureSupported() to make this work.

Returns whether or not the feature is supported if the backend is connected, or false if the backend is not connected.
