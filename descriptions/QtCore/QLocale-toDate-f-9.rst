.. sip:method-description::
    :status: todo
    :pysig: 482044ea5c5b74964abc5400e05b9cd9
    :realsig: (const QString&, QLocale::FormatType, int) const
    :digest: 7d96f866fe72e9f87e2d0921348c7c1c

Reads *string* as a date in a locale-specific *format*.

Parses *string* and returns the date it represents. The format of the date string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`).

Some locales use, particularly for :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat`, only the last two digits of the year. In such a case, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. In some cases, other fields may lead to the next or previous century being selected, to get a result consistent with all fields given. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for details.

**Note:** Month and day names, where used, must be given in the locale's language.

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
