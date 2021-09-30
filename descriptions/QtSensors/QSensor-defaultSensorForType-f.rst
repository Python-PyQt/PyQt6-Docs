.. sip:method-description::
    :status: todo
    :pysig: e9501ebb4868285b8a317efaae329f55
    :realsig: (const QByteArray&)
    :digest: 1939fdbb52ab529c8f9af0185116edc9

Returns the default sensor identifier for *type*. This is set in a config file and can be overridden if required. If no default is available the system will return the first registered sensor for *type*.

Note that there is special case logic to prevent the generic plugin's backends from becoming the default when another backend is registered for the same type. This logic means that a backend identifier starting with ``generic.`` will only be the default if no other backends have been registered for that type or if it is specified in ``Sensors.conf``.

.. seealso:: `Determining the default sensor for a type <https://doc.qt.io/qt-6/determining-the-default-sensor-for-a-type.html>`_.
