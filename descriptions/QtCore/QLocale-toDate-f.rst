.. sip:method-description::
    :status: todo
    :pysig: bde832d4e99f6c9ce7d868e858303a6a
    :realsig: (const QString&,QLocale::FormatType) const
    :digest: 04d062c57810ca800403af8be763ddc6

Reads *string* as a date in a locale-specific *format*.

Parses *string* and returns the date it represents. The format of the date string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`).

**Note:** Month and day names, where used, must be given in the locale's language.

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
