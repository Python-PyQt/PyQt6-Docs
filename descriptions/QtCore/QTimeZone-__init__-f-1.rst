.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 3442a3b8da42d9a0f4dd8c7688179da8

Creates a time zone instance with the requested IANA ID *ianaId*.

The ID must be one of the available system IDs or a valid UTC-with-offset ID, otherwise an invalid time zone will be returned.

This constructor is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`.
