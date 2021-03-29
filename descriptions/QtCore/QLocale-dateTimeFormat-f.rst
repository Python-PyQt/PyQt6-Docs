.. sip:method-description::
    :status: todo
    :pysig: 47629bd086b1b98e7b6adf82de758d9b
    :realsig: (QLocale::FormatType) const
    :digest: 1bbaa6ad094dae75f3df38186509ba17

Returns the date time format used for the current locale.

If *format* is :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`, the format will be elaborate, otherwise it will be short. For example, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat` for the ``en_US`` locale is ``dddd, MMMM d, yyyy h:mm:ss AP t``, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat` is ``M/d/yy h:mm AP``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toString`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
