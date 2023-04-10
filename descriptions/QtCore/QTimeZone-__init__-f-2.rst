.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: aabe5d9b855cf85273ded55ecccba9e7

Creates a time zone instance with the given offset, *offsetSeconds*, from UTC.

The *offsetSeconds* from UTC must be in the range -14 hours to +14 hours otherwise an invalid time zone will be returned.

This constructor is only available when feature ``timezone`` is enabled. The returned instance is equivalent to the lightweight time representation ``QTimeZone::fromSecondsAfterUtc(offsetSeconds)``, albeit implemented as a time zone.
