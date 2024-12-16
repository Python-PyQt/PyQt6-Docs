.. sip:method-description::
    :status: todo
    :pysig: a9b379fc65724ed5c75998c5855ec15f
    :realsig: (int)
    :digest: cead21e1049a724c53f557fb042afde8

Returns a list of all available IANA time zone IDs with a given standard time offset of *offsetSeconds*.

Where the given offset is supported, ``QTimeZone(offsetSeconds).id()`` is included in the list, even if it is not an IANA ID. This only arises when there is no IANA UTC-offset ID with the given offset.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.isTimeZoneIdAvailable`, QTimeZone(int).
