.. sip:method-description::
    :status: todo
    :pysig: 2b96497b7939e22eebbeb7313a135e65
    :realsig: (const QString&, QLocale::FormatType, int) const
    :digest: 62dd2fbe6f5236b449db851ad4966cf4

Reads *string* as a date-time in a locale-specific *format*.

Parses *string* and returns the date-time it represents. The format of the date string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`).

Some locales use, particularly for :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat`, only the last two digits of the year. In such a case, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. In some cases, other fields may lead to the next or previous century being selected, to get a result consistent with all fields given. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for details.

**Note:** Month and day names, where used, must be given in the locale's language. Any am/pm indicators used must match :sip:ref:`~PyQt6.QtCore.QLocale.amText` or :sip:ref:`~PyQt6.QtCore.QLocale.pmText`, ignoring case.

If the string could not be parsed, returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
