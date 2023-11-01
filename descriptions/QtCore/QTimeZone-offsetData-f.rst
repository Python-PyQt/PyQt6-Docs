.. sip:method-description::
    :status: todo
    :pysig: d03de0efeffef2d91ec115e9924b405c
    :realsig: (const QDateTime&) const
    :digest: fd3683bb61719197108be4f010e3c5c3

Returns the effective offset details at the given *forDateTime*.

This is the equivalent of calling :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation` and all three offset functions individually but is more efficient. If this data is not available for the given datetime, an invalid :sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData` will be returned with an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` as its ``atUtc``.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.standardTimeOffset`, :sip:ref:`~PyQt6.QtCore.QTimeZone.daylightTimeOffset`, :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.
