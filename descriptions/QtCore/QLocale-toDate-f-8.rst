.. sip:method-description::
    :status: todo
    :pysig: bf7af59f2d6457fd85461f08275cf8b6
    :realsig: (const QString&, const QString&, int) const
    :digest: a0182186ea6176e21652e0044f0053a9

Reads *string* as a date in the given *format*.

Parses *string* and returns the date it represents. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for the interpretation of *format*.

When *format* only specifies the last two digits of a year, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. In some cases, other fields may lead to the next or previous century being selected, to get a result consistent with all fields given. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for details.

**Note:** Month and day names, where used, must be given in the locale's language.

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
