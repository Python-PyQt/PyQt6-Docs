.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int*) const
    :digest: 83dd290ba836ea766cdde7fc4136adc1

Returns the ISO 8601 week number (1 to 53).

Returns 0 if the date is invalid. Otherwise, returns the week number for the date. If *yearNumber* is not ``nullptr`` (its default), stores the year as \*\ *yearNumber*.

In accordance with ISO 8601, each week falls in the year to which most of its days belong, in the Gregorian calendar. As ISO 8601's week starts on Monday, this is the year in which the week's Thursday falls. Most years have 52 weeks, but some have 53.

**Note:** \*\ *yearNumber* is not always the same as :sip:ref:`~PyQt6.QtCore.QDate.year`. For example, 1 January 2000 has week number 52 in the year 1999, and 31 December 2002 has week number 1 in the year 2003.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.isValid`.
