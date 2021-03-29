.. sip:enum-description::
    :status: todo
    :digest: 28768b83e97b2bc8e0075ce0062ec11f

This enum describes the different formats that can be used when converting :sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtCore.QTime`, and :sip:ref:`~PyQt6.QtCore.QDateTime` objects, as well as months and days, to strings specific to the locale.

**Note:** ``NarrowFormat`` might contain the same text for different months and days. It can even be an empty string if the locale doesn't support narrow names, so you should avoid using it for date formatting. Also, for the system locale this format is the same as ``ShortFormat``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.timeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.monthName`, :sip:ref:`~PyQt6.QtCore.QLocale.standaloneMonthName`, :sip:ref:`~PyQt6.QtCore.QLocale.dayName`, :sip:ref:`~PyQt6.QtCore.QLocale.standaloneDayName`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`.
