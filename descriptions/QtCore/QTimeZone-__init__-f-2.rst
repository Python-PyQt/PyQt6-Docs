.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: bedad3bcdc293ee380e70ad545f440cf

Creates a time zone instance with the given offset, *offsetSeconds*, from UTC.

The *offsetSeconds* from UTC must be in the range -16 hours to +16 hours otherwise an invalid time zone will be returned.

This constructor is only available when feature ``timezone`` is enabled. The returned instance is equivalent to the lightweight time representation ``QTimeZone::fromSecondsAfterUtc(offsetSeconds)``, albeit implemented as a time zone.

.. seealso:: MinUtcOffsetSecs, MaxUtcOffsetSecs.
