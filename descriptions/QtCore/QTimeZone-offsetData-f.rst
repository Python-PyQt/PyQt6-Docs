.. sip:method-description::
    :status: todo
    :pysig: d03de0efeffef2d91ec115e9924b405c
    :realsig: (const QDateTime&) const
    :digest: 10a682665160bcb714cf3bbdc9abcefd

Returns the effective offset details at the given *forDateTime*. This is the equivalent of calling :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`, etc individually but is more efficient.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.standardTimeOffset`, :sip:ref:`~PyQt6.QtCore.QTimeZone.daylightTimeOffset`, :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.
