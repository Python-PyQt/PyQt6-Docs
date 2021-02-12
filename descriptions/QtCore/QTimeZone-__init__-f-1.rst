.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 8756c9154f956fe92937a9a090183b08

Creates an instance of the requested time zone *ianaId*.

The ID must be one of the available system IDs or a valid UTC-with-offset ID, otherwise an invalid time zone will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`.
