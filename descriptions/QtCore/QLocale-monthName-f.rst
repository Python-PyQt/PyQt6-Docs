.. sip:method-description::
    :status: todo
    :pysig: 5aeddb0d884a40fb5e2304f6f17fb033
    :realsig: (int,QLocale::FormatType) const
    :digest: 0655c022fe59a36fc102da80c77c24f4

Returns the localized name of *month*, in the format specified by *type*.

For example, if the locale is ``en_US`` and *month* is 1, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat` will return ``January``. :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat` ``Jan``, and :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.NarrowFormat` ``J``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dayName`, :sip:ref:`~PyQt6.QtCore.QLocale.standaloneMonthName`.
