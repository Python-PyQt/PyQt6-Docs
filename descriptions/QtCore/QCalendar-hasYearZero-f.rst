.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 77ad021300200b43d2049d94622791ca

Returns ``true`` if this calendar has a year zero.

A calendar may represent years from its first year onwards but provide no way to describe years before its first; such a calendar has no year zero and is not proleptic.

A calendar which represents years before its first may number these years simply by following the usual integer counting, so that the year before the first is year zero, with negative-numbered years preceding this; such a calendar is proleptic and has a year zero. A calendar might also have a year zero (for example, the year of some great event, with subsequent years being the first year after that event, the second year after, and so on) without describing years before its year zero. Such a calendar would have a year zero without being proleptic.

Some calendars, however, represent years before their first by an alternate numbering; for example, the proleptic Gregorian calendar's first year is 1 CE and the year before it is 1 BCE, preceded by 2 BCE and so on. In this case, we use negative year numbers for this alternate numbering, with year -1 as the year before year 1, year -2 as the year before year -1 and so on. Such a calendar is proleptic but has no year zero.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.isProleptic`.
