.. sip:method-description::
    :status: todo
    :pysig: fd93e24386d7a93b002ed17f06b23584
    :realsig: (const QLocale&,int,int,QLocale::FormatType) const
    :digest: b9c674b074f553322270e303b5df167a

Returns a suitably localised standalone name for a month.

The month is indicated by a number, with *month* = 1 meaning the first month of the year and subsequent months numbered accordingly. Returns an empty string if the *month* number is unrecognized.

The *year* may be Unspecified, in which case the mapping from numbers to names for a typical year's months should be used. Some calendars have leap months that aren't always at the end of the year; their mapping of month numbers to names may then depend on the placement of a leap month. Thus the year should normally be specified, if known.

The name is returned in the form that would be used in isolation in the specified *locale*; the *format* determines how fully it shall be expressed (i.e. to what extent it is abbreviated).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.monthName`, :sip:ref:`~PyQt6.QtCore.QCalendar.maximumMonthsInYear`, :sip:ref:`~PyQt6.QtCore.QCalendar.dateTimeToString`.
