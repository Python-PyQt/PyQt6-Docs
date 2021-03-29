.. sip:method-description::
    :status: todo
    :pysig: 47629bd086b1b98e7b6adf82de758d9b
    :realsig: (QLocale::FormatType) const
    :digest: 3a18d9ae8627c8cf621d0e3e92e7348c

Returns the date format used for the current locale.

If *format* is :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`, the format will be elaborate, otherwise it will be short. For example, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat` for the ``en_US`` locale is ``dddd, MMMM d, yyyy``, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat` is ``M/d/yy``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
