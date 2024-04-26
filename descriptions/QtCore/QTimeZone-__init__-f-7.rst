.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: a47c793d1b859ce87c3b881d74f5ce28

Creates a time zone instance with the requested IANA ID *ianaId*.

The ID must be one of the available system IDs or a valid UTC-with-offset ID, otherwise an invalid time zone will be returned. For UTC-with-offset IDs, when they are not in fact IANA IDs, the ``id()`` of the resulting instance may differ from the ID passed to the constructor.

This constructor is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`, :sip:ref:`~PyQt6.QtCore.QTimeZone.id`.
