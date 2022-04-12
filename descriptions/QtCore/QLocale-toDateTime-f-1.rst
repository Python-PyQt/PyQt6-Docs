.. sip:method-description::
    :status: todo
    :pysig: bbf9933d450248e663b72f0d7b39b903
    :realsig: (const QString&,const QString&) const
    :digest: 76df3dc0c615e7874cb7a59cb02298ce

Reads *string* as a date-time in the given *format*.

Parses *string* and returns the date-time it represents. See :sip:ref:`~PyQt6.QtCore.QDateTime.fromString` for the interpretation of *format*.

**Note:** Month and day names, where used, must be given in the locale's language. Any am/pm indicators used must match :sip:ref:`~PyQt6.QtCore.QLocale.amText` or :sip:ref:`~PyQt6.QtCore.QLocale.pmText`, ignoring case.

If the string could not be parsed, returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`. If the string can be parsed and represents an invalid date-time (e.g. in a gap skipped by a time-zone transition), an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` is returned, whose toMSecsSinceEpoch() represents a near-by date-time that is valid. Passing that to fromMSecsSinceEpoch() will produce a valid date-time that isn't faithfully represented by the string parsed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
