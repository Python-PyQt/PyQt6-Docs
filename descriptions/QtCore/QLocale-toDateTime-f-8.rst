.. sip:method-description::
    :status: todo
    :pysig: 674fc530b9ec53375dd07af20aeb3e08
    :realsig: (const QString&, const QString&, int) const
    :digest: e5434413961e316e522303b950141fee

Reads *string* as a date-time in the given *format*.

Parses *string* and returns the date-time it represents. See :sip:ref:`~PyQt6.QtCore.QDateTime.fromString` for the interpretation of *format*.

When *format* only specifies the last two digits of a year, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. In some cases, other fields may lead to the next or previous century being selected, to get a result consistent with all fields given. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for details.

**Note:** Month and day names, where used, must be given in the locale's language. Any am/pm indicators used must match :sip:ref:`~PyQt6.QtCore.QLocale.amText` or :sip:ref:`~PyQt6.QtCore.QLocale.pmText`, ignoring case.

If the string could not be parsed, returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`. If the string can be parsed and represents an invalid date-time (e.g. in a gap skipped by a time-zone transition), an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` is returned, whose toMSecsSinceEpoch() represents a near-by date-time that is valid. Passing that to fromMSecsSinceEpoch() will produce a valid date-time that isn't faithfully represented by the string parsed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
