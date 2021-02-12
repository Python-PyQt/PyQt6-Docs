.. sip:method-description::
    :status: todo
    :pysig: 5aeddb0d884a40fb5e2304f6f17fb033
    :realsig: (int,QLocale::FormatType) const
    :digest: 1db14cf8191910a87fbb9796213ece7b

Returns the localized name of the *day* (where 1 represents Monday, 2 represents Tuesday and so on), in the format specified by *type*.

For example, if the locale is ``en_US`` and *day* is 1, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat` will return ``Monday``, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat` ``Mon``, and :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.NarrowFormat` ``M``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.monthName`, :sip:ref:`~PyQt6.QtCore.QLocale.standaloneDayName`.
