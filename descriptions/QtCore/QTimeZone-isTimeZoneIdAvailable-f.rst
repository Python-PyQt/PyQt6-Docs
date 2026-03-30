.. sip:method-description::
    :status: todo
    :pysig: 865c24f5e9df0906c2434bd9ef4cfa13
    :realsig: (const QByteArray&)
    :digest: 93c5954a8559092f384420fe96eb7c80

Returns ``true`` if a given time zone *ianaId* is available on this system.

This may include some non-IANA IDs, notably UTC-offset IDs, that are not listed in :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`.
