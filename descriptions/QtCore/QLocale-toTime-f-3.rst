.. sip:method-description::
    :status: todo
    :pysig: bcadb989f4bdaa947f6640bbb5b80c81
    :realsig: (const QString&, const QString&) const
    :digest: 05051764daaa0cd02128da6f64adae0c

Reads *string* as a time in the given *format*.

Parses *string* and returns the time it represents. See :sip:ref:`~PyQt6.QtCore.QTime.fromString` for the interpretation of *format*.

**Note:** Any am/pm indicators used must match :sip:ref:`~PyQt6.QtCore.QLocale.amText` or :sip:ref:`~PyQt6.QtCore.QLocale.pmText`, ignoring case.

If the time could not be parsed, returns an invalid time.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.timeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`.
