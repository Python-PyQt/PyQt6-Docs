.. sip:method-description::
    :status: todo
    :pysig: 22e9355fa66f9a58af8f4ee6a81ff093
    :realsig: (const QString&,QLocale::FormatType) const
    :digest: 84ff2e1778cad8e17ee998d239bde35d

Reads *string* as a date-time in a locale-specific *format*.

Parses *string* and returns the date-time it represents. The format of the date string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`).

**Note:** Month and day names, where used, must be given in the locale's language. Any am/pm indicators used must match :sip:ref:`~PyQt6.QtCore.QLocale.amText` or :sip:ref:`~PyQt6.QtCore.QLocale.pmText`, ignoring case.

If the string could not be parsed, returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
