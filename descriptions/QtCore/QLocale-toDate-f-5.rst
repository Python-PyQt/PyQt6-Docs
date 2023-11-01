.. sip:method-description::
    :status: todo
    :pysig: 2dbd73667cb82bd02e04bfb4b0a96cd1
    :realsig: (const QString&, const QString&) const
    :digest: 14a7682cdff241cca20230eba1c3abd1

Reads *string* as a date in the given *format*.

Parses *string* and returns the date it represents. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for the interpretation of *format*.

**Note:** Month and day names, where used, must be given in the locale's language.

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
