.. sip:method-description::
    :status: todo
    :pysig: 5aeddb0d884a40fb5e2304f6f17fb033
    :realsig: (int,QLocale::FormatType) const
    :digest: 170f57d4cde81d1fb23c244295894ac8

Returns the localized name of the *day* (where 1 represents Monday, 2 represents Tuesday and so on) that is used as a standalone text, in the format specified by *type*.

If the locale information does not specify the standalone day name then return value is the same as in :sip:ref:`~PyQt6.QtCore.QLocale.dayName`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dayName`, :sip:ref:`~PyQt6.QtCore.QLocale.standaloneMonthName`.
