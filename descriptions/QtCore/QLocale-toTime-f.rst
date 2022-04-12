.. sip:method-description::
    :status: todo
    :pysig: 851b74792d703d1281d06e84be3dbf88
    :realsig: (const QString&,QLocale::FormatType) const
    :digest: 77527f1464a9fcc125e9628c9f0a723e

Reads *string* as a time in a locale-specific *format*.

Parses *string* and returns the time it represents. The format of the time string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.timeFormat`).

**Note:** Any am/pm indicators used must match :sip:ref:`~PyQt6.QtCore.QLocale.amText` or :sip:ref:`~PyQt6.QtCore.QLocale.pmText`, ignoring case.

If the time could not be parsed, returns an invalid time.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.timeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`.
