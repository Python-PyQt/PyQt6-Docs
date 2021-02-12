.. sip:method-description::
    :status: todo
    :pysig: bbf9933d450248e663b72f0d7b39b903
    :realsig: (const QString&,const QString&) const
    :digest: 1aee598727f0d7e5aee0932ed38d1d3f

Parses the date/time string given in *string* and returns the time. See :sip:ref:`~PyQt6.QtCore.QDateTime.fromString` for information on the expressions that can be used with this function.

**Note:** The month and day names used must be given in the user's local language.

If the string could not be parsed, returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`. If the string can be parsed and represents an invalid date-time (e.g. in a gap skipped by a time-zone transition), an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` is returned, whose toMSecsSinceEpoch() represents a near-by date-time that is valid. Passing that to fromMSecsSinceEpoch() will produce a valid date-time that isn't faithfully represented by the string parsed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
