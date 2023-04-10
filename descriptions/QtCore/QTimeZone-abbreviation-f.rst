.. sip:method-description::
    :status: todo
    :pysig: 67ee2b41666e72cf350bc2e589a4b154
    :realsig: (const QDateTime&) const
    :digest: 2df37893e8ab718fef36f05f98c60cb0

Returns the time zone abbreviation at the given *atDateTime*. The abbreviation may change depending on DST or even historical events.

Note that the abbreviation is not guaranteed to be unique to this time zone and should not be used in place of the ID or display name.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName`.
