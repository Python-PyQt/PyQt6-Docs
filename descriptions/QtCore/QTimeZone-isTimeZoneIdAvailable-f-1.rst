.. sip:method-description::
    :status: todo
    :pysig: 1c22d44bea12141f421a1884cbebed91
    :realsig: (const QByteArray&)
    :digest: 93c5954a8559092f384420fe96eb7c80

Returns ``true`` if a given time zone *ianaId* is available on this system.

This may include some non-IANA IDs, notably UTC-offset IDs, that are not listed in :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`.
