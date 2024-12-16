.. sip:method-description::
    :status: todo
    :pysig: 67ee2b41666e72cf350bc2e589a4b154
    :realsig: (const QDateTime&) const
    :digest: 65bb12e224b50a2466bffed28d64fa48

Returns the time zone abbreviation at the given *atDateTime*.

The abbreviation may change depending on DST or even historical events.

**Note:** The abbreviation is not guaranteed to be unique to this time zone and should not be used in place of the ID or display name. The abbreviation may be localized, depending on the underlying operating system. To get consistent localization, use ``displayName(atDateTime, QTimeZone::ShortName, locale)``.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName`.
