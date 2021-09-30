.. sip:method-description::
    :status: todo
    :pysig: 9471a6907986bd629c9d09f90f2c8f04
    :realsig: (const QString&,const QVariant&)
    :digest: 47b4ef97a8ba8ea827ddb0b6267c850a

Sets the backend-specific property named *name* to *value*. Returns ``true`` on success, ``false`` otherwise. Backend-specific properties can be used to configure the positioning subsystem behavior at runtime. Supported backend-specific properties are listed and described in `Qt Positioning plugins#Default plugins <https://doc.qt.io/qt-6/qtpositioning-plugins.html#default-plugins>`_.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.backendProperty`.
