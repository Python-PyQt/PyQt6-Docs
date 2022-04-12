.. sip:method-description::
    :status: todo
    :pysig: e371e8fc1e62696de05c9576e4b347ce
    :realsig: (const QString&,const QString&) const
    :digest: 14a7682cdff241cca20230eba1c3abd1

Reads *string* as a date in the given *format*.

Parses *string* and returns the date it represents. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for the interpretation of *format*.

**Note:** Month and day names, where used, must be given in the locale's language.

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
